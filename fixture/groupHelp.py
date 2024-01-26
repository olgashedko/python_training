class GroupHelper:
    def __init__(self, app):
        self.app = app

    def return_to_group_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("group page").click()

    def create_new_group(self, group):
        wd = self.app.wd
        # go to group page
        self.open_group_page()
        # create new group
        wd.find_element_by_name("new").click()
        # fill group parameters
        self.fill_group_data(group)
        # submit group creation
        wd.find_element_by_name("submit").click()
        self.return_to_group_page()

    def delete_first_group(self):
        wd = self.app.wd
        # go to group page
        self.open_group_page()
        # click element
        self.select_first_group()
        # submit deletion
        wd.find_element_by_name("delete").click()
        self.return_to_group_page()

    def open_group_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("groups").click()

    def edit_first_group(self, group):
        wd = self.app.wd
        # go to group page
        self.open_group_page()
        self.select_first_group()
        # click edit button
        wd.find_element_by_name("edit").click()
        # fill group data
        self.fill_group_data(group)
        # submit changes
        wd.find_element_by_name("update").click()
        self.return_to_group_page()

    def select_first_group(self):
        wd = self.app.wd
        # select first group
        wd.find_element_by_name("selected[]").click()

    def fill_group_data(self, group):
        wd = self.app.wd
        self.add_text("group_name", group.group_name)
        self.add_text("group_header", group.group_header)
        self.add_text("group_footer", group.group_footer)

    def add_text(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def modify_first_group(self, group):
        wd = self.app.wd
        # go to group page
        self.open_group_page()
        self.select_first_group()
        # click edit button
        wd.find_element_by_name("edit").click()
        # fill group data
        self.fill_group_data(group)
        # submit changes
        wd.find_element_by_name("update").click()
        self.return_to_group_page()