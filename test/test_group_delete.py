import time
from random import randrange

from model.group import Group


def test_delete_arbitrary_group(app):
    if app.groupHelp.count() == 0:
        app.groupHelp.create_new_group(Group(group_name="group1"))
    old_groups = app.groupHelp.get_group_list()
    index = randrange(len(old_groups))
    app.groupHelp.delete_group_by_index(index)
    assert len(old_groups) - 1 == app.groupHelp.count()
    new_groups = app.groupHelp.get_group_list()
    old_groups[index:index+1] = []
    assert old_groups == new_groups
