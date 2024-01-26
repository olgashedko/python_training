import time

from model.group import Group


def test_edit_first_group(app):
    if app.groupHelp.count() == 0:
        app.groupHelp.create_new_group(Group(group_name="group1"))
    app.groupHelp.edit_first_group(Group(group_name="test", group_header="test", group_footer="test"))
