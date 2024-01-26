from model.contact import Contact


def test_delete_contact(app):
    if app.contactHelp.count() == 0:
        app.contactHelp.add_new_contact(Contact(firstname="Alex"))
    app.contactHelp.delete_first_contact()
