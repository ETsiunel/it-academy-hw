"""Homework_24"""


import time
import random
import string
import pytest
from selenium import webdriver
from selenium.common import TimeoutException
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from hw_24.source.locators import (AddUserLocators, LoginLocators,
                                   LogoutLocators, AddContactLocators,
                                   UpdateContactLocators, DeleteContactLocators)


@pytest.fixture(scope="module")
def driver():
    chrome_options = Options()
    chrome_options.add_argument('--start-maximized')
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=chrome_options)
    driver.implicitly_wait(10)
    yield driver
    driver.quit()


def random_char(char_num):
    return ''.join(random.choice(string.ascii_letters) for _ in range(char_num))


EMAIL = random_char(7) + '@test.com'
PASSWORD = random_char(11)


def test_signup(driver):
    driver.get(AddUserLocators.URL_add_user)
    driver.find_element(By.CSS_SELECTOR, AddUserLocators.signup_button).click()

    first_name = driver.find_element(By.CSS_SELECTOR, AddUserLocators.firstname_input_signup)
    first_name.clear()
    first_name.send_keys("TestFirstName")

    last_name = driver.find_element(By.CSS_SELECTOR, AddUserLocators.lastname_input_signup)
    last_name.clear()
    last_name.send_keys("TestLastName")

    email = driver.find_element(By.CSS_SELECTOR, AddUserLocators.email_input_signup)
    email.clear()
    email.send_keys(EMAIL)

    password = driver.find_element(By.CSS_SELECTOR, AddUserLocators.password_input_signup)
    password.clear()
    password.send_keys(PASSWORD)

    driver.find_element(By.CSS_SELECTOR, AddUserLocators.submit_button_signup).click()

    driver.find_element(By.CSS_SELECTOR, LogoutLocators.logout_button).click()


def test_login(driver):
    driver.get(LoginLocators.URL_login)

    email = driver.find_element(By.CSS_SELECTOR, LoginLocators.email_input_login)
    email.clear()
    email.send_keys(EMAIL)

    password = driver.find_element(By.CSS_SELECTOR, LoginLocators.password_input_login)
    password.clear()
    password.send_keys(PASSWORD)

    driver.find_element(By.CSS_SELECTOR, LoginLocators.submit_button_login).click()


def test_add_new_contact(driver):
    test_login(driver)

    driver.get(AddContactLocators.URL_add_contact)
    driver.find_element(By.CSS_SELECTOR, AddContactLocators.add_new_contact_button).click()

    first_name = driver.find_element(By.CSS_SELECTOR,
                                     AddContactLocators.firstname_input_add_contact)
    first_name.clear()
    first_name.send_keys("John")

    last_name = driver.find_element(By.CSS_SELECTOR, AddContactLocators.lastname_input_add_contact)
    last_name.clear()
    last_name.send_keys("Doe")

    birthdate = driver.find_element(By.CSS_SELECTOR, AddContactLocators.birthdate_add_contact)
    birthdate.clear()
    birthdate.send_keys("2000-01-01")

    email = driver.find_element(By.CSS_SELECTOR, AddContactLocators.email_input_add_contact)
    email.clear()
    email.send_keys("johndoe@example.com")

    phone = driver.find_element(By.CSS_SELECTOR, AddContactLocators.phone_input_add_contact)
    phone.clear()
    phone.send_keys("1234567890")

    street1 = driver.find_element(By.CSS_SELECTOR, AddContactLocators.street1_input_add_contact)
    street1.clear()
    street1.send_keys("123 Main St")

    street2 = driver.find_element(By.CSS_SELECTOR, AddContactLocators.street2_input_add_contact)
    street2.clear()
    street2.send_keys("Apt 4B")

    city = driver.find_element(By.CSS_SELECTOR, AddContactLocators.city_input_add_contact)
    city.clear()
    city.send_keys("Anytown")

    state_province = driver.find_element(By.CSS_SELECTOR,
                                         AddContactLocators.stateprovince_input_add_contact)
    state_province.clear()
    state_province.send_keys("State")

    postal_code = driver.find_element(By.CSS_SELECTOR,
                                      AddContactLocators.postalcode_input_add_contact)
    postal_code.clear()
    postal_code.send_keys("12345")

    country = driver.find_element(By.CSS_SELECTOR, AddContactLocators.country_input_add_contact)
    country.clear()
    country.send_keys("Country")

    driver.find_element(By.CSS_SELECTOR, AddContactLocators.submit_button_add_contact).click()

    try:
        WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR,
                                                 UpdateContactLocators.contact_table_body_row_edit))
        )
        contact_elements = driver.find_elements(By.CSS_SELECTOR,
                                                UpdateContactLocators.contact_table_body_row_edit)
        contact_found = False

        for contact in contact_elements:
            if "John Doe" in contact.text and "johndoe@example.com" in contact.text:
                contact_found = True
                break

        assert contact_found, "Contact John Doe not found."

    except TimeoutException:
        pytest.fail("Timed out waiting for contact to appear.")


def test_update_contact(driver):
    driver.get(AddContactLocators.URL_add_contact)
    contacts = driver.find_elements(By.CSS_SELECTOR,
                                    UpdateContactLocators.contact_table_body_row_edit)

    if contacts:
        contacts[0].click()
        driver.find_element(By.CSS_SELECTOR, UpdateContactLocators.edit_contact_button).click()
        time.sleep(2)

        first_name = driver.find_element(By.XPATH,
                                         UpdateContactLocators.firstname_input_edit_contact)
        first_name.clear()
        first_name.send_keys("Ann")

        last_name = driver.find_element(By.XPATH, UpdateContactLocators.lastname_input_edit_contact)
        last_name.clear()
        last_name.send_keys("Smith")

        birthdate = driver.find_element(By.XPATH, UpdateContactLocators.birthdate_edit_contact)
        birthdate.clear()
        birthdate.send_keys("2000-05-05")

        email = driver.find_element(By.XPATH, UpdateContactLocators.email_input_edit_contact)
        email.clear()
        email.send_keys("annesmith@example.com")

        phone = driver.find_element(By.XPATH, UpdateContactLocators.phone_input_edit_contact)
        phone.clear()
        phone.send_keys("0987654321")

        street1 = driver.find_element(By.XPATH, UpdateContactLocators.street1_input_edit_contact)
        street1.clear()
        street1.send_keys("456 Main St")

        street2 = driver.find_element(By.XPATH, UpdateContactLocators.street2_input_edit_contact)
        street2.clear()
        street2.send_keys("Apt 5C")

        city = driver.find_element(By.XPATH, UpdateContactLocators.city_input_edit_contact)
        city.clear()
        city.send_keys("Othertown")

        state_province = driver.find_element(By.XPATH,
                                             UpdateContactLocators.stateprovince_input_edit_contact)
        state_province.clear()
        state_province.send_keys("Province")

        postal_code = driver.find_element(By.XPATH,
                                          UpdateContactLocators.postalcode_input_edit_contact)
        postal_code.clear()
        postal_code.send_keys("54321")

        country = driver.find_element(By.XPATH, UpdateContactLocators.country_input_edit_contact)
        country.clear()
        country.send_keys("NewCountry")

        driver.find_element(By.CSS_SELECTOR,
                            UpdateContactLocators.submit_button_edit_contact).click()
        driver.find_element(By.CSS_SELECTOR,
                            UpdateContactLocators.return_to_contact_list_button).click()

        try:
            WebDriverWait(driver, 10).until(
                EC.presence_of_all_elements_located(
                    (By.CSS_SELECTOR, UpdateContactLocators.contact_table_body_row_edit))
            )
            contact_elements = driver.find_elements(
                By.CSS_SELECTOR, UpdateContactLocators.contact_table_body_row_edit)
            contact_found = False

            for contact in contact_elements:
                if "Ann Smith" in contact.text and "annesmith@example.com" in contact.text:
                    contact_found = True
                    break

            assert contact_found, "Contact Ann Smith not found."

        except TimeoutException:
            pytest.fail("Timed out waiting for contact to appear.")

    else:
        pytest.fail("No contacts available to update.")


def test_delete_contact(driver):
    driver.get(AddContactLocators.URL_add_contact)
    contacts = driver.find_elements(
        By.CSS_SELECTOR, DeleteContactLocators.contact_table_body_row_delete)
    if contacts:
        contacts[0].click()
        driver.find_element(By.CSS_SELECTOR, DeleteContactLocators.delete_contact_button).click()
        WebDriverWait(driver, 10).until(EC.alert_is_present())
        driver.switch_to.alert.accept()

        try:
            WebDriverWait(driver, 10).until_not(
                EC.presence_of_element_located((
                    By.CSS_SELECTOR, DeleteContactLocators.contact_table_body_row_delete)))
            contact_elements = (driver.find_elements
                                (By.CSS_SELECTOR,DeleteContactLocators.contact_table_body_row_delete))
            contact_found = any(
                "Ann Smith" in contact.text and "annesmith@example.com"
                in contact.text for contact in contact_elements)

            assert not contact_found, "Contact Ann Smith was not deleted."

        except TimeoutException:
            pytest.fail("Timed out waiting for deleting contact")

    else:
        pytest.fail("No contacts available to delete.")


if __name__ == "__main__":
    pytest.main()
