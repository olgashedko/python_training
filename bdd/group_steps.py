import random

from pytest_bdd import given, when, then, parsers
from model.group import Group


@given('a group list', target_fixture='group_list')
def group_list(db):
    return db.get_group_list()


@given(parsers.parse('a group with {name}, {header} and {footer}'), target_fixture='new_group')
def new_group(name, header, footer):
    return Group(group_name=name, group_header=header, group_footer=footer)


@when('I add the group to the list', target_fixture='add_new_group')
def add_new_group(app, new_group):
    app.groupHelp.create_new_group(new_group)


@then('the new group list is equal to the olf list with the added group', target_fixture='verify_group_added')
def verify_group_added(db, group_list, new_group):
    old_groups = group_list
    new_groups = db.get_group_list()
    old_groups.append(new_group)
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)


@given('a non-empty group list', target_fixture='non_empty_group_list')
def non_empty_group_list(db, app):
    if len(db.get_group_list()) == 0:
        app.groupHelp.create_new_group(Group(group_name='some name'))
    return db.get_group_list()


@given('a random group from the list', target_fixture='random_group')
def random_group(non_empty_group_list):
    return random.choice(non_empty_group_list)


@when('I delete the group from the list', target_fixture='delete_group')
def delete_group(app, random_group):
    app.groupHelp.delete_group_by_id(random_group.group_id)


@then('the new group list is equal to the olf list without the deleted group', target_fixture='verify_group_deleted')
def verify_group_deleted(db, non_empty_group_list, random_group, app, check_ui):
    old_groups = non_empty_group_list
    new_groups = db.get_group_list()
    assert len(old_groups) -1 == len(new_groups)
    old_groups.remove(random_group)
    assert old_groups == new_groups
    if check_ui:
        assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
