import time


def test_delete_first_group(app):
    app.session.login(username="admin", password="secret")
    app.groupHelp.delete_first_group()
    app.session.logout()
    time.sleep(1)