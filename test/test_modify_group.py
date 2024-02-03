import time

from model.group import Group


#def test_modify_group_name(app):
#    if app.groupHelp.count() == 0:
#        app.groupHelp.create_new_group(Group(group_name="group1"))
#    old_groups = app.groupHelp.get_group_list()
#    app.groupHelp.modify_first_group(Group(group_name="New name"))
#    new_groups = app.groupHelp.get_group_list()
#    assert len(old_groups) == len(new_groups)


def test_modify_group_header(app):
    if app.groupHelp.count() == 0:
        app.groupHelp.create_new_group(Group(group_name="group1"))
    old_groups = app.groupHelp.get_group_list()
    group1 = Group(group_name="New header")
    group1.group_id = old_groups[0].group_id
    app.groupHelp.modify_first_group(group1)
    new_groups = app.groupHelp.get_group_list()
    assert len(old_groups) == len(new_groups)
    old_groups[0] = group1
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)

#def test_modify_group_footer(app):
#    if app.groupHelp.count() == 0:
#        app.groupHelp.create_new_group(Group(group_name="group1"))
#    old_groups = app.groupHelp.get_group_list()
#    app.groupHelp.modify_first_group(Group(group_footer="New footer"))
#    new_groups = app.groupHelp.get_group_list()
#    assert len(old_groups) == len(new_groups)
