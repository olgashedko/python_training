import random

from model.contact import Contact
from model.group import Group


def test_add_contact_to_group(app, db, check_ui):
    if len(db.get_group_list()) == 0:
        app.groupHelp.create_new_group(Group(group_name="group1"))
    if len(db.get_group_list()) == 0:
        app.contactHelp.add_new_contact(Contact(firstname="Alex"))
    old_contacts = db.get_contact_list()
    contact = random.choice(old_contacts)
    old_groups = db.get_group_list()
    group = random.choice(old_groups)
    app.contactHelp.add_contact_to_group(contact, group)