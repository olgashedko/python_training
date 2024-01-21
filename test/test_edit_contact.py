import time

from model.contact import Contact


def test_edit_first_contact(app):
    app.session.login(username="admin", password="secret")
    app.contactHelp.edit_first_contact(
        Contact(firstname="Ivan", middlename="Ivanovich", lastname="Ivanov", nickname="Vanya", company="Company",
                title="title", address="SPb, str 1-1-1", home="111-11-11", mobile="+7921-111-11-11",
                work="222-22-22", fax="222-22-22", email="test@test.com", email2="test2@test.com",
                email3="test3@test.com", homepage="localpage", bday="11", byear="2000", bmonth="November",
                aday="23", amonth="November", ayear="2000"))
    app.session.logout()
    time.sleep(1)