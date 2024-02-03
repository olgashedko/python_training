from model.contact import Contact


def test_delete_contact(app):
    if app.contactHelp.count() == 0:
        app.contactHelp.add_new_contact(Contact(firstname="Alex"))
    old_contacts = app.contactHelp.get_contact_list()
    app.contactHelp.delete_first_contact()
    new_contacts = app.contactHelp.get_contact_list()
    assert len(old_contacts) - 1 == len(new_contacts)
    old_contacts[0:1] = []
    assert old_contacts == new_contacts

