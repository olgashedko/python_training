import random
import time
from random import randrange

from model.group import Group


def test_modify_group_name(app, db, check_ui):
    if len(db.get_group_list()) == 0:
        app.groupHelp.create_new_group(Group(group_name="group1"))
    old_groups = db.get_group_list()
    group = random.choice(old_groups)
    group1 = Group(group_name="New name")
    group1.group_id = group.group_id
    app.groupHelp.modify_group_by_id(group1, group.group_id)
    new_groups = db.get_group_list()
    for index in range(0, len(old_groups)):
        if old_groups[index].group_id == group.group_id:
            old_groups[index] = group1
    assert old_groups == new_groups
    if check_ui:
        assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)

