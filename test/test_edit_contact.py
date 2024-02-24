import random
from random import randrange

from model.contact import Contact


def test_edit_contact(app, db, check_ui):
    if len(db.get_group_list()) == 0:
        app.contactHelp.add_new_contact(Contact(firstname="Alex"))
    old_contacts = db.get_contact_list()
    contact = random.choice(old_contacts)
    contact1 = Contact(firstname="Ivan", middlename="Ivanovich", lastname="Ivanov", nickname="Vanya", company="Company",
                title="title", address="SPb, str 1-1-1", home="111-11-11", mobile="+7921-111-11-11",
                work="222-22-22", fax="222-22-22", email="test@test.com", email2="test2@test.com",
                email3="test3@test.com", homepage="localpage", bday="11", byear="2000", bmonth="November",
                aday="23", amonth="November", ayear="2000")
    contact1.contact_id = contact.contact_id
    app.contactHelp.edit_contact_by_id(contact1, contact.contact_id)
    new_contacts = db.get_contact_list()
    for index in range(0, len(old_contacts)):
        if old_contacts[index].contact_id == contact.contact_id:
            old_contacts[index] = contact1
    assert old_contacts == new_contacts
    if check_ui:
        assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.contactHelp.get_contact_list(), key=Contact.id_or_max)

