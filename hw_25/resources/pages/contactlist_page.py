"""Contact List page"""


import time
from selenium.webdriver.common.by import By
from hw_25.resources.pages.base_page import BasePage
from hw_25.resources.locators.add_contact_locators import AddContactLocators
from hw_25.resources.locators.update_contact_locators import UpdateContactLocators
from hw_25.resources.locators.delete_contact_locators import DeleteContactLocators


class ContactListPage(BasePage):
    def add_new_contact(self, contact_data):
        self.find_element_visible(By.CSS_SELECTOR,
                                  AddContactLocators.add_new_contact_button).click()
        self._fill_contact_form(contact_data)
        self.find_element_visible(By.CSS_SELECTOR,
                                  AddContactLocators.submit_button_add_contact).click()

    def update_contact(self, contact_data):
        contacts = self.find_elements_visible(By.CSS_SELECTOR,
                                              UpdateContactLocators.contact_table_body_row_edit)
        if contacts:
            contacts[0].click()
            self.find_element_visible(By.CSS_SELECTOR, UpdateContactLocators.edit_contact_button).click()
            self._fill_contact_form(contact_data, is_update=True)
            submit_button = self.find_element_visible(By.CSS_SELECTOR,
                                                      UpdateContactLocators.submit_button_edit_contact)
            submit_button.click()
            return_to_contact_list_button = self.find_element_visible(
                By.CSS_SELECTOR, UpdateContactLocators.return_to_contact_list_button)
            return_to_contact_list_button.click()
        else:
            raise Exception("No contacts available to update.")

    def delete_contact(self):
        contacts = self.find_elements_visible(By.CSS_SELECTOR,
                                              DeleteContactLocators.contact_table_body_row_delete)
        if contacts:
            contacts[0].click()
            self.find_element_visible(By.CSS_SELECTOR,
                                      DeleteContactLocators.delete_contact_button).click()
            alert = self.driver.switch_to.alert
            alert.accept()
        else:
            raise Exception("No contacts available to delete.")

    def _fill_contact_form(self, contact_data, is_update=False):
        locators = UpdateContactLocators if is_update else AddContactLocators

        def fill_field(locator, value):
            element = self.find_element_visible(By.CSS_SELECTOR, locator)
            element.clear()
            element.send_keys(value)

        time.sleep(1)
        fill_field(locators.firstname_input, contact_data['first_name'])
        time.sleep(1)
        fill_field(locators.lastname_input, contact_data['last_name'])
        time.sleep(1)
        fill_field(locators.birthdate_input, contact_data['birthdate'])
        fill_field(locators.email_input, contact_data['email'])
        fill_field(locators.phone_input, contact_data['phone'])
        fill_field(locators.street1_input, contact_data['street1'])
        fill_field(locators.street2_input, contact_data['street2'])
        fill_field(locators.city_input, contact_data['city'])
        fill_field(locators.stateprovince_input, contact_data['state_province'])
        fill_field(locators.postalcode_input, contact_data['postal_code'])
        fill_field(locators.country_input, contact_data['country'])
