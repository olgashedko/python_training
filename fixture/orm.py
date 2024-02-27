from pony.orm import *

from model.contact import Contact
from model.group import Group
from pymysql.converters import decoders


class ORMFixture:
    db = Database()

    class ORMGroup(db.Entity):
        _table_ = 'group_list'
        id = PrimaryKey(int, column='group_id')
        name = Optional(str, column='group_name')
        header = Optional(str, column='group_header')
        footer = Optional(str, column='group_footer')
        contacts = Set(lambda: ORMFixture.ORMContact, table="address_in_groups", column="id", reverse="groups",
                       lazy=True)

    class ORMContact(db.Entity):
        _table_ = 'addressbook'
        id = PrimaryKey(int, column='id')
        firstname = Optional(str, column='firstname')
        lastname = Optional(str, column='lastname')
        address = Optional(str, column='address')
        home = Optional(str, column='home')
        work = Optional(str, column='work')
        mobile = Optional(str, column='mobile')
        email = Optional(str, column='email')
        email2 = Optional(str, column='email2')
        email3 = Optional(str, column='email3')
        groups = Set(lambda: ORMFixture.ORMGroup, table="address_in_groups", column="group_id",
                     reverse="contacts", lazy=True)

    def __init__(self, host, name, user, password):
        self.db.bind('mysql', host=host, database=name, user=user, password=password)
        self.db.generate_mapping()
        sql_debug(True)

    def convert_groups_to_model(self, groups):
        def convert(group):
            return Group(group_id=str(group.id), group_name=group.name,
                         group_header=group.header, group_footer=group.footer)

        return list(map(convert, groups))


    def convert_contacts_to_model(self, contacts):
        def convert(contact):
            return Contact(contact_id=str(contact.id), firstname=contact.firstname, lastname=contact.lastname,
                           address=contact.address, home=contact.home, work=contact.work, mobile=contact.mobile,
                           email=contact.email, email2=contact.email2, email3=contact.email3)

        return list(map(convert, contacts))

    @db_session
    def get_group_list(self):
        return self.convert_groups_to_model(select(g for g in ORMFixture.ORMGroup))

    @db_session
    def get_contact_list(self):
        return self.convert_contacts_to_model(select(c for c in ORMFixture.ORMContact))

    @db_session
    def get_contacts_in_group(self, group):
        orm_group = list(select(g for g in ORMFixture.ORMGroup if g.id == group.group_id))[0]
        return self.convert_contacts_to_model(orm_group.contacts)

    @db_session
    def get_contacts_not_in_group(self, group):
        orm_group = list(select(g for g in ORMFixture.ORMGroup if g.id == group.group_id))[0]
        return self.convert_contacts_to_model(
            select(c for c in ORMFixture.ORMContact if orm_group not in c.groups))

    @db_session
    def get_contacts_not_in_any_group(self):
        return self.convert_contacts_to_model(
            select(c for c in ORMFixture.ORMContact if len(c.groups) == 0))

    @db_session
    def get_groups_with_contacts(self):
        return self.convert_groups_to_model(select(g for g in ORMFixture.ORMGroup if len(g.contacts) != 0))
