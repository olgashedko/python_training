# -*- coding: utf-8 -*-
import pytest
from model.group import Group


def test_add_new_group(app, json_groups):
    group = json_groups
    old_groups = app.groupHelp.get_group_list()
    app.groupHelp.create_new_group(group)
    assert len(old_groups) + 1 == app.groupHelp.count()
    new_groups = app.groupHelp.get_group_list()
    old_groups.append(group)
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)

