# -*- coding: utf-8 -*-
from model.contact import Contact


def test_add_new_contact(app):
    app.contactHelp.add_new_contact(
        Contact(firstname="Petr", middlename="Petrovich", lastname="Petrov", nickname="Petya", company="Company",
                title="title", address="SPb, str 1-1-1", home="111-11-11", mobile="+7921-111-11-11",
                work="222-22-22", fax="222-22-22", email="test@test.com", email2="test2@test.com",
                email3="test3@test.com", homepage="localpage", bday="11", byear="2000", bmonth="November",
                aday="23", amonth="November", ayear="2000"))
