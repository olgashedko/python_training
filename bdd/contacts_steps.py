import random

from pytest_bdd import given, when, then, parsers
from model.contact import Contact


@given('a contact list', target_fixture='contact_list')
def contact_list(db):
    return db.get_contact_list()


@given(parsers.parse('a contact with {firstname}, {lastname}, {middlename}, {work}, {home} and {mobile}'), target_fixture='new_contact')
def new_contact(firstname, lastname, middlename, work, home, mobile):
    return Contact(firstname=firstname, middlename=middlename, lastname=lastname, home=home, mobile=mobile, work=work)


@when('I add the contact to the list', target_fixture='add_new_contact')
def add_new_group(app, new_contact):
    app.contactHelp.add_new_contact(new_contact)


@then('the new contact list is equal to the old list with the added contact', target_fixture='verify_contact_added')
def verify_group_added(db, contact_list, new_contact):
    old_contacts = contact_list
    new_contacts = db.get_contact_list()
    old_contacts.append(new_contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)


@given('a non-empty contact list', target_fixture='non_empty_contact_list')
def non_empty_contact_list(db, app):
    if len(db.get_contact_list()) == 0:
        app.contactHelp.add_new_contact(Contact(firstname='some name'))
    return db.get_contact_list()


@given('a random contact from the list', target_fixture='random_contact')
def random_group(non_empty_contact_list):
    return random.choice(non_empty_contact_list)


@when('I delete the contact from the list', target_fixture='delete_contact')
def delete_group(app, random_contact):
    app.contactHelp.delete_contact_by_id(random_contact.contact_id)


@then('the new contact list is equal to the old list without the deleted contact', target_fixture='verify_contact_deleted')
def verify_group_deleted(db, non_empty_contact_list, random_contact, app, check_ui):
    old_contacts = non_empty_contact_list
    new_contacts = db.get_contact_list()
    assert len(old_contacts) -1 == len(new_contacts)
    old_contacts.remove(random_contact)
    assert old_contacts == new_contacts
    if check_ui:
        assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)