import time

from model.group import Group


def test_modify_group_name(app):
    app.groupHelp.modify_first_group(Group(group_name="New name"))


def test_modify_group_header(app):
    app.groupHelp.modify_first_group(Group(group_header="New header"))


def test_modify_group_footer(app):
    app.groupHelp.modify_first_group(Group(group_footer="New footer"))
