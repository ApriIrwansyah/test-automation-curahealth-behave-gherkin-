from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from time import sleep
from pages.base_page import BasePage


class HistoryAppointment(BasePage):
    
    def navigate_to_history(self):
        self.click_element((By.XPATH, "//a[@id='menu-toggle']"))
        self.click_element((By.XPATH, "//a[normalize-space()='History']"))
        
    def get_appointment_record(self):
        return self.wait_for_element((By.XPATH, "//h2[normalize-space()='History']")).text