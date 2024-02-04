from random import randrange

from model.contact import Contact


def test_edit_first_contact(app):
    if app.contactHelp.count() == 0:
        app.contactHelp.add_new_contact(Contact(firstname="Alex"))
    old_contacts = app.contactHelp.get_contact_list()
    index = randrange(len(old_contacts))
    contact1 = Contact(firstname="Ivan", middlename="Ivanovich", lastname="Ivanov", nickname="Vanya", company="Company",
                title="title", address="SPb, str 1-1-1", home="111-11-11", mobile="+7921-111-11-11",
                work="222-22-22", fax="222-22-22", email="test@test.com", email2="test2@test.com",
                email3="test3@test.com", homepage="localpage", bday="11", byear="2000", bmonth="November",
                aday="23", amonth="November", ayear="2000")
    contact1.contact_id = old_contacts[index].contact_id
    app.contactHelp.edit_contact_by_index(contact1, index)
    assert len(old_contacts) == app.contactHelp.count()
    new_contacts = app.contactHelp.get_contact_list()
    old_contacts[index] = contact1
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)

