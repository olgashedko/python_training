import time

from model.contact import Contact


def test_delete_contact(app):
    app.session.login(username="admin", password="secret")
    app.contactHelp.delete_first_contact()
    app.session.logout()
    time.sleep(1)