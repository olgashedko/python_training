import re

from model.contact import Contact


def test_phones_on_home_page(app):
    contact_from_home_page = app.contactHelp.get_contact_list()[1]
    contact_from_edit_page = app.contactHelp.get_contact_info_from_edit_page(1)
    assert contact_from_home_page.all_contacts_from_home_page == merge_phones(contact_from_edit_page)


def test_phones_on_view_page(app):
    contact_from_view_page = app.contactHelp.get_contact_info_from_view_page(1)
    contact_from_edit_page = app.contactHelp.get_contact_info_from_edit_page(1)
    assert contact_from_view_page.home == contact_from_edit_page.home
    assert contact_from_view_page.work == contact_from_edit_page.work
    assert contact_from_view_page.mobile == contact_from_edit_page.mobile


def clear(s):
    return re.sub("[() -]", "", s)


def merge_phones(contact):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear(x), filter(lambda x: x is not None,
                                                           [contact.home, contact.mobile, contact.work]))))

