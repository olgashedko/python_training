# -*- coding: utf-8 -*-
import random
import string
import time

import pytest

from model.contact import Contact


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + " " * 10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


def random_phone(maxlen):
    symbols = string.digits + " " * 10
    return "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


testdata = [
               Contact(firstname=random_string("firstname", 10), middlename=random_string("middlename", 10),
                       lastname=random_string("lastname", 10), home=random_phone(12),
                       work=random_phone(12), mobile=random_phone(12))
               for i in range(5)] + [
               Contact(firstname="Petr", middlename="Petrovich", lastname="Petrov", nickname="Petya", company="Company",
                       title="title", address="SPb, str 1-1-1", home="111-11-11", mobile="+7921-111-11-11",
                       work="222-22-22", fax="222-22-22", email="test@test.com", email2="test2@test.com",
                       email3="test3@test.com", homepage="localpage", bday="11", byear="2000", bmonth="November",
                       aday="23", amonth="November", ayear="2000")]


@pytest.mark.parametrize("contact", testdata, ids=[repr(x) for x in testdata])
def test_add_new_contact(app, contact):
    old_contacts = app.contactHelp.get_contact_list()
    app.contactHelp.add_new_contact(contact)
    assert len(old_contacts) + 1 == app.contactHelp.count()
    new_contacts = app.contactHelp.get_contact_list()
    old_contacts.append(contact)
    time.sleep(2)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
