import time

from model.group import Group


def test_modify_group_name(app):
    if app.groupHelp.count() == 0:
        app.groupHelp.create_new_group(Group(group_name="group1"))
    app.groupHelp.modify_first_group(Group(group_name="New name"))


def test_modify_group_header(app):
    if app.groupHelp.count() == 0:
        app.groupHelp.create_new_group(Group(group_name="group1"))
    app.groupHelp.modify_first_group(Group(group_header="New header"))


def test_modify_group_footer(app):
    if app.groupHelp.count() == 0:
        app.groupHelp.create_new_group(Group(group_name="group1"))
    app.groupHelp.modify_first_group(Group(group_footer="New footer"))
