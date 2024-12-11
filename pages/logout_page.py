from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from time import sleep
from pages.base_page import BasePage

class LogoutPage(BasePage):
    # URL = "https://katalon-demo-cura.herokuapp.com/"

    # def navigate(self):
    #     self.driver.get(self.URL)

    # def click_logout(self):
    #     self.click_element((By.ID, "btn-make-appointment"))

    # def form_login(self, username, password):
    #     self.enter_text((By.ID, "txt-username"), username)
    #     sleep(1)
    #     self.enter_text((By.ID, "txt-password"), password)
    #     sleep(1)
    #     self.click_element((By.ID, "btn-login"))
        
    def navigate_to_logout(self):
        self.click_element((By.XPATH, "//a[@id='menu-toggle']"))
        sleep(1)
        self.click_element((By.XPATH, "//a[normalize-space()='Logout']"))
        sleep(1)
        
    def get_logout_success(self):
        return self.wait_for_element((By.XPATH, "//h1[normalize-space()='CURA Healthcare Service']")).text