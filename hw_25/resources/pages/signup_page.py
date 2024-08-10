"""Signup page"""


from selenium.webdriver.common.by import By
from hw_25.resources.pages.base_page import BasePage
from hw_25.resources.locators.signup_locators import SignupLocators


class SignupPage(BasePage):
    def signup(self, first_name, last_name, email, password):
        self.driver.find_element(By.CSS_SELECTOR, SignupLocators.firstname_input_signup).clear()
        self.driver.find_element(By.CSS_SELECTOR, SignupLocators.firstname_input_signup).send_keys(first_name)
        self.driver.find_element(By.CSS_SELECTOR, SignupLocators.lastname_input_signup).clear()
        self.driver.find_element(By.CSS_SELECTOR, SignupLocators.lastname_input_signup).send_keys(last_name)
        self.driver.find_element(By.CSS_SELECTOR, SignupLocators.email_input_signup).clear()
        self.driver.find_element(By.CSS_SELECTOR, SignupLocators.email_input_signup).send_keys(email)
        self.driver.find_element(By.CSS_SELECTOR, SignupLocators.password_input_signup).clear()
        self.driver.find_element(By.CSS_SELECTOR, SignupLocators.password_input_signup).send_keys(password)
        self.driver.find_element(By.CSS_SELECTOR, SignupLocators.submit_button_signup).click()

    def is_signup_successful(self):
        return "Logout" in self.driver.page_source
