# -*- coding: utf-8 -*-

from model.group import Group


def test_add_new_group(app):
    app.groupHelp.create_new_group(Group(group_name="test", group_header="test", group_footer="test"))


def test_add_empty_group(app):
    app.groupHelp.create_new_group(Group(group_name="", group_header="", group_footer=""))

