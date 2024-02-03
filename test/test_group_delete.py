import time
from model.group import Group


def test_delete_first_group(app):
    if app.groupHelp.count() == 0:
        app.groupHelp.create_new_group(Group(group_name="group1"))
    old_groups = app.groupHelp.get_group_list()
    app.groupHelp.delete_first_group()
    new_groups = app.groupHelp.get_group_list()
    assert len(old_groups) - 1 == len(new_groups)
    old_groups[0:1] = []
    assert old_groups == new_groups
