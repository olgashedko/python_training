import random
import re

from model.contact import Contact


def test_contact_data_on_home_page(app, db):
    def clean(contact):
        return Contact(contact_id=contact.contact_id, firstname=contact.firstname.strip(" "),
                       lastname=contact.lastname.strip(" "), home=contact.home, mobile=contact.mobile,
                       work=contact.work, address=contact.address, email=contact.email, email2=contact.email2,
                       email3=contact.email3)
    contacts_from_home_page = sorted(app.contactHelp.get_contact_list(), key=Contact.id_or_max)
    contacts_from_db = sorted(map(clean, db.get_contact_list()), key=Contact.id_or_max)
    for index in range(0, len(contacts_from_home_page)):
        assert contacts_from_home_page[index].firstname == contacts_from_db[index].firstname
        assert contacts_from_home_page[index].lastname == contacts_from_db[index].lastname
        assert contacts_from_home_page[index].full_address == contacts_from_db[index].address.replace("\r", "")
        assert contacts_from_home_page[index].all_contacts_from_home_page == merge_phones(contacts_from_db[index])
        assert contacts_from_home_page[index].all_emails == merge_emails(contacts_from_db[index])


def clear(s):
    return re.sub("[() -]", "", s)


def merge_phones(contact):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear(x), filter(lambda x: x is not None,
                                                           [contact.home, contact.mobile, contact.work]))))


def merge_emails(contact):
    return "\n".join(filter(lambda x: x != "",
                            filter(lambda x: x is not None, [contact.email, contact.email2, contact.email3])))
