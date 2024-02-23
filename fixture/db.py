import pymysql

from model.contact import Contact
from model.group import Group


class DbFixture:
    def __init__(self, host, name, user, password):
        self.host = host
        self.name = name
        self.user = user
        self.password = password
        self.connection = pymysql.connect(host=host, database=name, user=user, password=password, autocommit=True)

    def get_group_list(self):
        list1 = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("select group_id, group_name, group_header, group_footer from group_list")
            for row in cursor:
                (group_id, group_name, group_header, group_footer) = row
                list1.append(Group(group_id=str(group_id), group_name=group_name, group_header=group_header,
                                   group_footer=group_footer))
        finally:
            cursor.close()
        return list1

    def get_contact_list(self):
        list1 = []
        cursor = self.connection.cursor()
        try:
            cursor.execute(
                "select firstname, middlename, lastname, id, mobile, home, work, address, email, email2, email3 from "
                "addressbook")
            for row in cursor:
                (firstname, middlename, lastname, id, mobile, home, work, address, email, email2, email3) = row
                list1.append(Contact(firstname=firstname, lastname=lastname, contact_id=str(id),
                                     all_contacts_from_home_page=home + mobile + work, full_address=address,
                                     all_emails=email+email2+email3))
        finally:
            cursor.close()
        return list1

    def destroy(self):
        self.connection.close()
