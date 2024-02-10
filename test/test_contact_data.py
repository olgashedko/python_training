import random
import re

from model.contact import Contact


def test_contact_data_on_home_page(app):
    index = random.randrange(len(app.contactHelp.get_contact_list()))
    print(str(index))
    contact_from_home_page = app.contactHelp.get_contact_list()[index]
    contact_from_edit_page = app.contactHelp.get_contact_info_from_edit_page(index)
    assert contact_from_home_page.firstname == contact_from_edit_page.firstname
    assert contact_from_home_page.lastname == contact_from_edit_page.lastname
    assert contact_from_home_page.address == contact_from_edit_page.address
    assert contact_from_home_page.all_contacts_from_home_page == merge_phones(contact_from_edit_page)
    assert contact_from_home_page.all_emails == merge_emails(contact_from_edit_page)


def clear(s):
    return re.sub("[() -]", "", s)


def merge_phones(contact):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear(x), filter(lambda x: x is not None,
                                                           [contact.home, contact.mobile, contact.work]))))


def merge_emails(contact):
    return "\n".join(filter(lambda x: x != "",
                            filter(lambda x: x is not None, [contact.email, contact.email2, contact.email3])))
