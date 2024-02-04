# -*- coding: utf-8 -*-
from model.contact import Contact


def test_add_new_contact(app):
    old_contacts = app.contactHelp.get_contact_list()
    contact1 = Contact(firstname="Petr", middlename="Petrovich", lastname="Petrov", nickname="Petya", company="Company",
                title="title", address="SPb, str 1-1-1", home="111-11-11", mobile="+7921-111-11-11",
                work="222-22-22", fax="222-22-22", email="test@test.com", email2="test2@test.com",
                email3="test3@test.com", homepage="localpage", bday="11", byear="2000", bmonth="November", aday="23", amonth="November", ayear="2000")
    app.contactHelp.add_new_contact(contact1)
    assert len(old_contacts) + 1 == app.contactHelp.count()
    new_contacts = app.contactHelp.get_contact_list()
    old_contacts.append(contact1)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)

