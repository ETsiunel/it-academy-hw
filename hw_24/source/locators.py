"""Locators"""


class AddUserLocators:
    URL_add_user = "https://thinking-tester-contact-list.herokuapp.com/login"
    signup_button = '#signup'
    firstname_input_signup = '#firstName'
    lastname_input_signup = '#lastName'
    email_input_signup = "#email"
    password_input_signup = "#password"
    submit_button_signup = '#submit'


class LoginLocators:
    URL_login = "https://thinking-tester-contact-list.herokuapp.com/login"
    email_input_login = "#email"
    password_input_login = "#password"
    submit_button_login = '#submit'


class LogoutLocators:
    logout_button = '#logout'


class AddContactLocators:
    URL_add_contact = "https://thinking-tester-contact-list.herokuapp.com/contactList"
    add_new_contact_button = '#add-contact'
    firstname_input_add_contact = '#firstName'
    lastname_input_add_contact = '#lastName'
    birthdate_add_contact = '#birthdate'
    email_input_add_contact = '#email'
    phone_input_add_contact = '#phone'
    street1_input_add_contact = '#street1'
    street2_input_add_contact = '#street2'
    city_input_add_contact = '#city'
    stateprovince_input_add_contact = '#stateProvince'
    postalcode_input_add_contact = '#postalCode'
    country_input_add_contact = '#country'
    submit_button_add_contact = '#submit'


class UpdateContactLocators:
    contact_table_body_row_edit = '[class="contactTableBodyRow"]'
    edit_contact_button = '#edit-contact'
    firstname_input_edit_contact = '//input[@id="firstName"]'
    lastname_input_edit_contact = '//input[@id="lastName"]'
    birthdate_edit_contact = '//input[@id="birthdate"]'
    email_input_edit_contact = '//input[@id="email"]'
    phone_input_edit_contact = '//input[@id="phone"]'
    street1_input_edit_contact = '//input[@id="street1"]'
    street2_input_edit_contact = '//input[@id="street2"]'
    city_input_edit_contact = '//input[@id="city"]'
    stateprovince_input_edit_contact = '//input[@id="stateProvince"]'
    postalcode_input_edit_contact = '//input[@id="postalCode"]'
    country_input_edit_contact = '//input[@id="country"]'
    submit_button_edit_contact = '#submit'
    return_to_contact_list_button = '#return'


class DeleteContactLocators:
    contact_table_body_row_delete = '[class="contactTableBodyRow"]'
    delete_contact_button = '#delete'
