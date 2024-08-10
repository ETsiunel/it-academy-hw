"""Constants"""


import random
import string


class Urls:
    URL_login = "https://thinking-tester-contact-list.herokuapp.com/login"
    URL_contact_list = "https://thinking-tester-contact-list.herokuapp.com/contactList"


class UserCredentials:
    EMAIL = ''.join(random.choice(string.ascii_letters) for _ in range(7)) + '@test.com'
    PASSWORD = ''.join(random.choice(string.ascii_letters) for _ in range(11))
