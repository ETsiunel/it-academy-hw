"""Constants"""


import random
import string


class Urls:
    URL_login = "https://thinking-tester-contact-list.herokuapp.com/login"
    URL_contact_list = "https://thinking-tester-contact-list.herokuapp.com/contactList"


class UserCredentials:
    def random_char(self, char_num):
        return ''.join(random.choice(string.ascii_letters) for _ in range(char_num))

    EMAIL = random_char(7) + '@test.com'
    PASSWORD = random_char(11)
