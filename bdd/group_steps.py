from pytest_bdd import given, when, then
from model.group import Group


@given('a group list', target_fixture='group_list')
def group_list(db):
    return db.get_group_list()


@given('a group with <name>, <header> and <footer>', target_fixture='new_group')
def new_group(name, header, footer):
    return Group(group_name=name, group_header=header, group_footer=footer)


@when('I add the group to the list', target_fixture='add_new_group')
def add_new_group(app, new_group):
    app.groupHelper.create_new_group(new_group)


@then('the new group list is equal to the olf list with the added group', target_fixture='verify_group_added')
def verify_group_added(db, group_list, new_group):
    old_groups = group_list
    new_groups = db.get_group_list()
    old_groups.append(new_group)
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
