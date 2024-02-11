# -*- coding: utf-8 -*-
import random
import string

import pytest

from model.group import Group


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + " " * 10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


testdata = [Group(group_name="", group_header="", group_footer="")] + [
            Group(group_name=random_string("name", 10), group_header=random_string("header", 20),
                  group_footer=random_string("footer", 20))
            for i in range(5)
            ]


@pytest.mark.parametrize("group", testdata, ids=[repr(x) for x in testdata])
def test_add_new_group(app, group):
    old_groups = app.groupHelp.get_group_list()
    app.groupHelp.create_new_group(group)
    assert len(old_groups) + 1 == app.groupHelp.count()
    new_groups = app.groupHelp.get_group_list()
    old_groups.append(group)
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)

