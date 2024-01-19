# -*- coding: utf-8 -*-
import pytest
from group import Group
from application import Application


@pytest.fixture()
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_new_group(app):
    app.login(username="admin", password="secret")
    app.create_new_group(Group(group_name="test", group_header="test", group_footer="test"))
    app.logout()


def test_add_empty_group(app):
    app.login(username="admin", password="secret")
    app.create_new_group(Group(group_name="", group_header="", group_footer=""))
    app.logout()
