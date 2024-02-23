import random
import time
from random import randrange

from model.group import Group


def test_delete_arbitrary_group(app, db, check_ui):
    if len(db.get_group_list()) == 0:
        app.groupHelp.create_new_group(Group(group_name="group1"))
    old_groups = db.get_group_list()
    group = random.choice(old_groups)
    app.groupHelp.delete_group_by_id(group.group_id)
    new_groups = db.get_group_list()
    old_groups.remove(group)
    assert old_groups == new_groups
    if check_ui:
        assert sorted(new_groups, key=Group.id_or_max) == sorted(app.groupHelp.get_group_list(), key=Group.id_or_max)
