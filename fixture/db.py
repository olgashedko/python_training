import pymysql

from model.group import Group


class DbFixture:
    def __init__(self, host, name, user, password):
        self.host = host
        self.name = name
        self.user = user
        self.password = password
        self.connection = pymysql.connect(host=host, database=name, user=user, password=password, autocommit=True)

    def get_group_list(self):
        list1 = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("select group_id, group_name, group_header, group_footer from group_list")
            for row in cursor:
                (group_id, group_name, group_header, group_footer) = row
                list1.append(Group(group_id=str(group_id), group_name=group_name, group_header=group_header, group_footer=group_footer))
        finally:
            cursor.close()
        return list1

    def destroy(self):
        self.connection.close()
