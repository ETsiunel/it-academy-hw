"""Base page"""


from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def find_element_visible(self, by, value):
        element = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((by, value))
        )
        return element

    def find_elements_visible(self, by, value):
        elements = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_all_elements_located((by, value))
        )
        return elements

    def wait_page_to_load(self):
        WebDriverWait(self.driver, 10).until(
            lambda driver: driver.execute_script('return document.readyState') == 'complete'
        )
