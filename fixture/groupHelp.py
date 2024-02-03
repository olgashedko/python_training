from model.group import Group


class GroupHelper:
    def __init__(self, app):
        self.app = app

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
        self.open_group_page()

    def delete_first_group(self):
        wd = self.app.wd
        # go to group page
        self.open_group_page()
        # click element
        self.select_first_group()
        # submit deletion
        wd.find_element_by_name("delete").click()
        self.open_group_page()

    def open_group_page(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("group.php") and len(wd.find_elements_by_name("new")) > 0):
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
        self.open_group_page()

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
        self.open_group_page()

    def count(self):
        wd = self.app.wd
        self.open_group_page()
        return len(wd.find_elements_by_name("selected[]"))

    def get_group_list(self):
        wd = self.app.wd
        self.open_group_page()
        group_list = []
        for element in wd.find_elements_by_css_selector("span.group"):
            text = element.text
            id = element.find_element_by_name("selected[]").get_attribute("value")
            group_list.append(Group(group_name=text, group_id=id))
        return group_list
