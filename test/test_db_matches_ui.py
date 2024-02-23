from model.group import Group


def test_group_list(app, db):
    ui_list = app.groupHelp.get_group_list()
    db_list = map(clean, db.get_group_list())
    assert sorted(ui_list, key=Group.id_or_max) == sorted(db_list, key=Group.id_or_max)


def clean(group):
    return Group(group_id=group.group_id, group_name=group.group_name.strip())
