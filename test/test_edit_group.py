import time

from model.group import Group


def test_edit_first_group(app):
    app.groupHelp.edit_first_group(Group(group_name="test", group_header="test", group_footer="test"))
