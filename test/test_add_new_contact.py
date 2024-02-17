# -*- coding: utf-8 -*-
import random
import string
import time

import pytest

from model.contact import Contact
from data.contacts import testdata


@pytest.mark.parametrize("contact", testdata, ids=[repr(x) for x in testdata])
def test_add_new_contact(app, contact):
    old_contacts = app.contactHelp.get_contact_list()
    app.contactHelp.add_new_contact(contact)
    assert len(old_contacts) + 1 == app.contactHelp.count()
    new_contacts = app.contactHelp.get_contact_list()
    old_contacts.append(contact)
    time.sleep(2)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
