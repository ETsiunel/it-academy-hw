"""Signup page"""


from selenium.webdriver.common.by import By
from hw_25.resources.pages.base_page import BasePage
from hw_25.resources.locators.signup_locators import SignupLocators


class SignupPage(BasePage):
    def signup(self, first_name, last_name, email, password):
        firstname_input = self.driver.find_element(By.CSS_SELECTOR,
                                                   SignupLocators.firstname_input_signup)
        firstname_input.clear()
        firstname_input.send_keys(first_name)

        lastname_input = self.driver.find_element(By.CSS_SELECTOR,
                                                  SignupLocators.lastname_input_signup)
        lastname_input.clear()
        lastname_input.send_keys(last_name)

        email_input = self.driver.find_element(By.CSS_SELECTOR,
                                               SignupLocators.email_input_signup)
        email_input.clear()
        email_input.send_keys(email)

        password_input = self.driver.find_element(By.CSS_SELECTOR,
                                                  SignupLocators.password_input_signup)
        password_input.clear()
        password_input.send_keys(password)

        self.driver.find_element(By.CSS_SELECTOR, SignupLocators.submit_button_signup).click()

    def is_signup_successful(self):
        return "Logout" in self.driver.page_source
