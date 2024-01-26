import time
from model.group import Group


def test_delete_first_group(app):
    if app.groupHelp.count() == 0:
        app.groupHelp.create_new_group(Group(group_name="group1"))
    app.groupHelp.delete_first_group()
