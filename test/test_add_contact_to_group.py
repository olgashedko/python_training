import random

from fixture.orm import ORMFixture
from model.contact import Contact
from model.group import Group

db1 = ORMFixture(host="127.0.0.1", name="addressbook", user="root", password="")


def test_add_contact_to_group(app, db, check_ui):
    if len(db.get_group_list()) == 0:
        app.groupHelp.create_new_group(Group(group_name="group1"))
    if len(db.get_contact_list()) == 0:
        app.contactHelp.add_new_contact(Contact(firstname="Alex"))
    old_contacts = db1.get_contacts_not_in_any_group()
    contact = random.choice(old_contacts)
    old_groups = db.get_group_list()
    group = random.choice(old_groups)
    old_contacts_in_group = db1.get_contacts_in_group(group)
    app.contactHelp.add_contact_to_group(contact, group)
    new_contacts_in_group = db1.get_contacts_in_group(group)
    assert contact not in old_contacts_in_group and contact in new_contacts_in_group
