# -*- coding: utf-8 -*-
import time

from model.group import Group


def test_add_new_group(app):
    app.session.login(username="admin", password="secret")
    app.groupHelp.create_new_group(Group(group_name="test", group_header="test", group_footer="test"))
    app.session.logout()
    time.sleep(1)


def test_add_empty_group(app):
    app.session.login(username="admin", password="secret")
    app.groupHelp.create_new_group(Group(group_name="", group_header="", group_footer=""))
    app.session.logout()
    time.sleep(1)
