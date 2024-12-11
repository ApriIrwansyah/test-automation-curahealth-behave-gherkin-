from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from time import sleep

class LoginPage(BasePage):
    URL = "https://katalon-demo-cura.herokuapp.com/"

    def navigate(self):
        self.driver.get(self.URL)

    def click_login(self):
        self.click_element((By.ID, "btn-make-appointment"))

    def perform_login(self, username, password):
        self.enter_text((By.ID, "txt-username"), username)
        sleep(1)
        self.enter_text((By.ID, "txt-password"), password)
        sleep(1)
        self.click_element((By.ID, "btn-login"))