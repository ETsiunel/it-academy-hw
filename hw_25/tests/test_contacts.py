"""Tests for full flow: signup-login-add_contact-update_contact-delete_contact"""


import logging
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from hw_25.tests.test_data.constants import Urls, UserCredentials
from hw_25.tests.test_data.test_data import (TestDataUser, TestDataAddContact,
                                             TestDataUpdateContact)
from hw_25.resources.pages.login_page import LoginPage
from hw_25.resources.pages.signup_page import SignupPage
from hw_25.resources.pages.contactlist_page import ContactListPage
from hw_25.resources.locators.logout_locators import LogoutLocators
from hw_25.resources.locators.add_contact_locators import AddContactLocators
from hw_25.resources.locators.update_contact_locators import UpdateContactLocators
from hw_25.resources.locators.delete_contact_locators import DeleteContactLocators

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


@pytest.fixture(scope="module")
def driver():
    chrome_options = Options()
    chrome_options.add_argument('--start-maximized')
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=chrome_options)
    driver.implicitly_wait(10)
    yield driver
    driver.quit()


def test_precondition_signup(driver):
    logging.info("Starting signup test")
    driver.get(Urls.URL_login)
    login_page = LoginPage(driver)
    login_page.go_to_signup()

    signup_page = SignupPage(driver)
    signup_page.signup(TestDataUser.firstname_user, TestDataUser.lastname_user,
                       UserCredentials.EMAIL, UserCredentials.PASSWORD)

    logging.info("Signup test completed successfully")

    driver.find_element(By.CSS_SELECTOR, LogoutLocators.logout_button).click()


def test_precondition_login(driver):
    logging.info("Starting login test")
    driver.get(Urls.URL_login)
    login_page = LoginPage(driver)
    login_page.login(UserCredentials.EMAIL, UserCredentials.PASSWORD)

    logging.info("Login test completed successfully")


def test_add_new_contact(driver):
    logging.info("Starting add new contact test")
    driver.get(Urls.URL_contact_list)
    contact_list_page = ContactListPage(driver)
    contact_data = {
        'first_name': TestDataAddContact.firstname_contact,
        'last_name': TestDataAddContact.lastname_contact,
        'birthdate': TestDataAddContact.birthdate_contact,
        'email': TestDataAddContact.email_contact,
        'phone': TestDataAddContact.phone_contact,
        'street1': TestDataAddContact.street1_contact,
        'street2': TestDataAddContact.street2_contact,
        'city': TestDataAddContact.city_contact,
        'state_province': TestDataAddContact.state_contact,
        'postal_code': TestDataAddContact.postalcode_contact,
        'country': TestDataAddContact.country_contact
    }

    contact_list_page.add_new_contact(contact_data)

    contact_elements = driver.find_elements(By.CSS_SELECTOR,
                                            AddContactLocators.contact_table_body_row_add)
    contact_found = any(
        TestDataAddContact.firstname_contact in contact.text and
        TestDataAddContact.lastname_contact in contact.text
        for contact in contact_elements
    )

    assert contact_found, "Contact not found."

    logging.info("Add new contact test completed successfully")


def test_update_contact(driver):
    logging.info("Starting update contact test")
    driver.get(Urls.URL_contact_list)
    contact_list_page = ContactListPage(driver)
    contact_data = {
        'first_name': TestDataUpdateContact.firstname_contact,
        'last_name': TestDataUpdateContact.lastname_contact,
        'birthdate': TestDataUpdateContact.birthdate_contact,
        'email': TestDataUpdateContact.email_contact,
        'phone': TestDataUpdateContact.phone_contact,
        'street1': TestDataUpdateContact.street1_contact,
        'street2': TestDataUpdateContact.street2_contact,
        'city': TestDataUpdateContact.city_contact,
        'state_province': TestDataUpdateContact.state_contact,
        'postal_code': TestDataUpdateContact.postalcode_contact,
        'country': TestDataUpdateContact.country_contact
    }

    contact_list_page.update_contact(contact_data)

    contact_elements = driver.find_elements(By.CSS_SELECTOR,
                                            UpdateContactLocators.contact_table_body_row_edit)
    contact_found = any(
        TestDataUpdateContact.firstname_contact in contact.text and
        TestDataUpdateContact.lastname_contact in contact.text
        for contact in contact_elements
    )

    assert contact_found, "Contact not found."

    logging.info("Update contact test completed successfully")


def test_delete_contact(driver):
    logging.info("Starting delete contact test")
    driver.get(Urls.URL_contact_list)
    contact_list_page = ContactListPage(driver)
    contact_list_page.delete_contact()

    contact_elements = driver.find_elements(By.CSS_SELECTOR,
                                            DeleteContactLocators.contact_table_body_row_delete)
    contact_found = any(
        TestDataUpdateContact.firstname_contact in contact.text and
        TestDataUpdateContact.lastname_contact in contact.text
        for contact in contact_elements
    )

    assert not contact_found, "Contact was not deleted."

    logging.info("Delete contact test completed successfully")
