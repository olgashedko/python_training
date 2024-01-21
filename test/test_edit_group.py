import time

from model.group import Group


def test_edit_first_group(app):
    app.session.login(username="admin", password="secret")
    app.groupHelp.edit_first_group(Group(group_name="test", group_header="test", group_footer="test"))
    app.session.logout()
    time.sleep(1)
