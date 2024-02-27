import random

from fixture.orm import ORMFixture
from model.contact import Contact
from model.group import Group

db1 = ORMFixture(host="127.0.0.1", name="addressbook", user="root", password="")


def test_delete_contact_from_group(app, db, check_ui):
    # if any contacts with group is absent, create it
    if len(db.get_group_list()) == 0:
        app.groupHelp.create_new_group(Group(group_name="group1"))
    if len(db.get_contact_list()) == 0:
        app.contactHelp.add_new_contact(Contact(firstname="Alex"))
    if len(db1.get_contacts_not_in_any_group()) == len(db.get_contact_list()):
        contacts = db.get_contact_list()
        contact = random.choice(contacts)
        old_groups = db.get_group_list()
        group = random.choice(old_groups)
        app.contactHelp.add_contact_to_group(contact, group)
    #select contact for group deletion
    groups_with_contacts = db1.get_groups_with_contacts()
    group2 = random.choice(groups_with_contacts)
    contacts_in_group_before_deletion = db1.get_contacts_in_group(group2)
    contact2 = random.choice(contacts_in_group_before_deletion)
    #delete selected contact from group
    app.contactHelp.delete_contact_from_group(contact2, group2)
    contacts_in_group_after_deletion = db1.get_contacts_in_group(group2)
    assert contact2 in contacts_in_group_before_deletion and contact2 not in contacts_in_group_after_deletion
