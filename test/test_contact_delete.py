import random
from random import randrange

from model.contact import Contact


def test_delete_contact(app, db, check_ui):
    if len(db.get_group_list()) == 0:
        app.contactHelp.add_new_contact(Contact(firstname="Alex"))
    old_contacts = db.get_contact_list()
    contact = random.choice(old_contacts)
    app.contactHelp.delete_contact_by_id(contact.contact_id)
    new_contacts = db.get_contact_list()
    old_contacts.remove(contact)
    assert old_contacts == new_contacts
    if check_ui:
        assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.contactHelp.get_contact_list(), key=Contact.id_or_max)


