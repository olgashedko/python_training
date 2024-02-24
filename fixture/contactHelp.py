import re

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

from model.contact import Contact


class ContactHelper:
    def __init__(self, app):
        self.app = app

    def go_home_page(self):
        wd = self.app.wd
        if not (wd.current_url.endswith(self.app.base_url)):
            wd.find_element_by_link_text("home").click()

    def add_new_contact(self, contact):
        wd = self.app.wd
        # go to new contact page
        self.go_to_new_contact_page()
        # fill contact data
        self.fill_contact_data(contact)
        wd.find_element_by_xpath("//div[@id='content']/form/input[20]").click()
        self.go_home_page()
        self.contact_cache = None

    def go_to_new_contact_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("add new").click()

    def delete_first_contact(self):
        self.delete_contact_by_index(0)

    def delete_contact_by_index(self, index):
        wd = self.app.wd
        # go to contact page
        self.go_home_page()
        # click element
        wd.find_elements_by_name("selected[]")[index].click()
        # submit deletion
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        self.go_home_page()
        self.contact_cache = None

    def delete_contact_by_id(self, id):
        wd = self.app.wd
        # go to contact page
        self.go_home_page()
        # click element
        wd.find_element_by_css_selector("input[value='%s" % id).click()
        # submit deletion
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        self.go_home_page()
        self.contact_cache = None

    def edit_first_contact(self, contact):
        self.edit_contact_by_index(contact, 0)

    def edit_contact_by_index(self, contact, index):
        wd = self.app.wd
        self.open_contact_to_edit_by_index(index)
        # fill contact data
        self.fill_contact_data(contact)
        wd.find_element_by_name("update").click()
        self.go_home_page()
        self.contact_cache = None

    def open_contact_to_edit_by_index(self, index):
        wd = self.app.wd
        # go to home page
        self.go_home_page()
        # click change first contact icon
        wd.find_elements_by_xpath("//img[@alt='Edit']")[index].click()
        time.sleep(0.5)

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

    def count(self):
        wd = self.app.wd
        self.go_home_page()
        return len(wd.find_elements_by_name("selected[]"))

    contact_cache = None

    def get_contact_list(self):
        if self.contact_cache is None:
            wd = self.app.wd
            self.go_home_page()
            self.contact_cache = []
            for element in wd.find_elements_by_name("entry"):
                first_name = element.find_element(By.CSS_SELECTOR, "td:nth-child(3)").text
                last_name = element.find_element(By.CSS_SELECTOR, "td:nth-child(2)").text
                id = element.find_element_by_name("selected[]").get_attribute("value")
                all_phones = element.find_element(By.CSS_SELECTOR, "td:nth-child(6)").text
                address = element.find_element(By.CSS_SELECTOR, "td:nth-child(4)").text
                all_emails = element.find_element(By.CSS_SELECTOR, "td:nth-child(5)").text
                self.contact_cache.append(Contact(firstname=first_name, lastname=last_name, contact_id=id,
                                                  all_contacts_from_home_page=all_phones, full_address=address,
                                                  all_emails=all_emails))
        return list(self.contact_cache)

    def get_contact_info_from_edit_page(self, index):
        wd = self.app.wd
        self.open_contact_to_edit_by_index(index)
        firstname = wd.find_element_by_name("firstname").get_attribute("value")
        lastname = wd.find_element_by_name("lastname").get_attribute("value")
        id = wd.find_element_by_name("id").get_attribute("value")
        homephone = wd.find_element_by_name("home").get_attribute("value")
        workphone = wd.find_element_by_name("work").get_attribute("value")
        mobilephone = wd.find_element_by_name("mobile").get_attribute("value")
        email = wd.find_element_by_name("email").get_attribute("value")
        email2 = wd.find_element_by_name("email2").get_attribute("value")
        email3 = wd.find_element_by_name("email3").get_attribute("value")
        return Contact(firstname=firstname, lastname=lastname, contact_id=id, home=homephone, work=workphone,
                       mobile=mobilephone, email=email, email2=email2, email3=email3)


    def get_contact_info_from_view_page(self, index):
        wd = self.app.wd
        self.open_contact_view_by_index(index)
        text = wd.find_element_by_id("content").text
        homephone = re.search("H: (.*)", text).group(1)
        workphone = re.search("W: (.*)", text).group(1)
        mobilephone = re.search("M: (.*)", text).group(1)
        return Contact(home=homephone, work=workphone,
                       mobile=mobilephone)

    def open_contact_view_by_index(self, index):
        wd = self.app.wd
        # go to home page
        self.go_home_page()
        # click change first contact icon
        wd.find_elements_by_xpath("//img[@alt='Details']")[index].click()


