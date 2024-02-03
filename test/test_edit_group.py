import time

from model.group import Group


def test_edit_first_group(app):
    if app.groupHelp.count() == 0:
        app.groupHelp.create_new_group(Group(group_name="group1"))
    old_groups = app.groupHelp.get_group_list()
    app.groupHelp.edit_first_group(Group(group_name="test", group_header="test", group_footer="test"))
    new_groups = app.groupHelp.get_group_list()
    assert len(old_groups) == len(new_groups)
