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
        self.group_cache = None

    def delete_first_group(self, index):
        self.delete_group_by_index(0)

    def delete_group_by_index(self, index):
        wd = self.app.wd
        # go to group page
        self.open_group_page()
        # click element
        self.select_group_by_index(index)
        # submit deletion
        wd.find_element_by_name("delete").click()
        self.open_group_page()
        self.group_cache = None

    def delete_group_by_id(self, id):
        wd = self.app.wd
        # go to group page
        self.open_group_page()
        # click element
        self.select_group_by_id(id)
        # submit deletion
        wd.find_element_by_name("delete").click()
        self.open_group_page()
        self.group_cache = None

    def open_group_page(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("group.php") and len(wd.find_elements_by_name("new")) > 0):
            wd.find_element_by_link_text("groups").click()

    def select_group_by_index(self, index):
        wd = self.app.wd
        # select first group
        wd.find_elements_by_name("selected[]")[index].click()

    def select_group_by_id(self, id):
        wd = self.app.wd
        # select first group
        wd.find_element_by_css_selector("input[value='%s" % id).click()

    def select_first_group(self):
        self.select_group_by_index(0)

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
        self.modify_group_by_index(group, 0)

    def modify_group_by_index(self, group, index):
        wd = self.app.wd
        # go to group page
        self.open_group_page()
        self.select_group_by_index(index)
        # click edit button
        wd.find_element_by_name("edit").click()
        # fill group data
        self.fill_group_data(group)
        # submit changes
        wd.find_element_by_name("update").click()
        self.open_group_page()
        self.group_cache = None

    def count(self):
        wd = self.app.wd
        self.open_group_page()
        return len(wd.find_elements_by_name("selected[]"))

    group_cache = None

    def get_group_list(self):
        if self.group_cache is None:
            wd = self.app.wd
            self.open_group_page()
            self.group_cache = []
            for element in wd.find_elements_by_css_selector("span.group"):
                text = element.text
                id = element.find_element_by_name("selected[]").get_attribute("value")
                self.group_cache.append(Group(group_name=text, group_id=id))
        return list(self.group_cache)
