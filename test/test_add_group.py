# -*- coding: utf-8 -*-

from model.group import Group


def test_add_new_group(app):
    old_groups = app.groupHelp.get_group_list()
    app.groupHelp.create_new_group(Group(group_name="test", group_header="test", group_footer="test"))
    new_groups = app.groupHelp.get_group_list()
    assert len(old_groups) + 1 == len(new_groups)


def test_add_empty_group(app):
    old_groups = app.groupHelp.get_group_list()
    app.groupHelp.create_new_group(Group(group_name="", group_header="", group_footer=""))
    new_groups = app.groupHelp.get_group_list()
    assert len(old_groups) + 1 == len(new_groups)