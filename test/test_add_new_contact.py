# -*- coding: utf-8 -*-
import time
from model.contact import Contact


def test_add_new_contact(app, json_contact, db, check_ui):
    contact = json_contact
    old_contacts = db.get_contact_list()
    app.contactHelp.add_new_contact(contact)
    new_contacts = db.get_contact_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
    if check_ui:
        assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.contactHelp.get_contact_list(), key=Contact.id_or_max)