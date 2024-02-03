from sys import maxsize


class Contact:
    def __init__(self, firstname=None, middlename=None, lastname=None, nickname=None, company=None, title=None, address=None, home=None, mobile=None, work=None, fax=None, email=None, email2=None, email3=None, homepage=None, bday=None, byear=None, bmonth=None, aday=None, amonth=None, ayear=None, contact_id=None):
        self.firstname = firstname
        self.middlename = middlename
        self.lastname = lastname
        self.nickname = nickname
        self.title = title
        self.company = company
        self.address = address
        self.home = home
        self.mobile = mobile
        self.work = work
        self.fax = fax
        self.email = email
        self.email2 = email2
        self.email3 = email3
        self.homepage = homepage
        self.bday = bday
        self.bmonth = bmonth
        self.byear = byear
        self.aday = aday
        self.amonth = amonth
        self.ayear = ayear
        self.contact_id = contact_id

    def __repr__(self):
        return "%s%s%s" % (self.firstname, self.lastname, self.contact_id)

    def __eq__(self, other):
        return (
                    self.contact_id is None or other.contact_id is None or self.contact_id == other.contact_id) and self.firstname == other.firstname and self.lastname == other.lastname

    def id_or_max(self):
        if self.contact_id:
            return int(self.contact_id)
        else:
            return maxsize

