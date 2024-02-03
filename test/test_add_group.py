# -*- coding: utf-8 -*-


from model.group import Group


def test_add_new_group(app):
    old_groups = app.groupHelp.get_group_list()
    group1 = Group(group_name="test", group_header="test", group_footer="test")
    app.groupHelp.create_new_group(group1)
    new_groups = app.groupHelp.get_group_list()
    assert len(old_groups) + 1 == len(new_groups)
    old_groups.append(group1)
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)


def test_add_empty_group(app):
    old_groups = app.groupHelp.get_group_list()
    group1 = Group(group_name="", group_header="", group_footer="")
    app.groupHelp.create_new_group(group1)
    new_groups = app.groupHelp.get_group_list()
    assert len(old_groups) + 1 == len(new_groups)
    old_groups.append(group1)
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
