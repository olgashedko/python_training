from selenium.webdriver.support.ui import Select
import time


class ContactHelper:
    def __init__(self, app):
        self.app = app

    def go_home_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("home").click()

    def add_new_contact(self, contact):
        wd = self.app.wd
        # go to new contact page
        self.go_to_new_contact_page()
        # fill contact data
        self.fill_contact_data(contact)
        wd.find_element_by_xpath("//div[@id='content']/form/input[20]").click()
        self.go_home_page()

    def go_to_new_contact_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("add new").click()

    def delete_first_contact(self):
        wd = self.app.wd
        # go to contact page
        self.go_home_page()
        # click element
        wd.find_element_by_name("selected[]").click()
        # submit deletion
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        self.go_home_page()

    def edit_first_contact(self, contact):
        wd = self.app.wd
        # go to home page
        self.go_home_page()
        # click change first contact icon
        wd.find_element_by_xpath("//img[@alt='Edit']").click()
        time.sleep(0.5)
        # fill contact data
        self.fill_contact_data(contact)
        wd.find_element_by_name("update").click()
        self.go_home_page()

    def fill_contact_data(self, contact):
        wd = self.app.wd
        self.add_text("firstname", contact.firstname)
        self.add_text("middlename", contact.middlename)
        self.add_text("lastname", contact.lastname)
        self.add_text("nickname", contact.nickname)
        self.add_text("title", contact.title)
        self.add_text("company", contact.company)
        self.add_text("address", contact.address)
        self.add_text("home", contact.home)
        self.add_text("mobile", contact.mobile)
        self.add_text("work", contact.work)
        self.add_text("fax", contact.fax)
        self.add_text("email", contact.email)
        self.add_text("email2", contact.email2)
        self.add_text("email3", contact.email3)
        self.add_text("homepage", contact.homepage)
        self.select_value("bday", contact.bday)
        self.select_value("bmonth", contact.bmonth)
        self.add_text("byear", contact.byear)
        self.select_value("aday", contact.aday)
        self.select_value("amonth", contact.amonth)
        self.add_text("ayear", contact.ayear)

    def add_text(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def select_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            Select(wd.find_element_by_name(field_name)).select_by_visible_text(text)
