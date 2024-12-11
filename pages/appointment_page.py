# pages/booking_page.py
from selenium.webdriver.common.by import By
from time import sleep
from pages.base_page import BasePage

class BookingPage(BasePage):
    URL = 'https://katalon-demo-cura.herokuapp.com/'
    
    def navigate(self):
        self.driver.get(self.URL)
    
    def click_login(self):
        self.click_element((By.ID, "btn-make-appointment"))
    def login(self, username, password):
        self.enter_text((By.ID, "txt-username"), username)
        sleep(1)
        self.enter_text((By.ID, "txt-password"), password)
        sleep(1)
        self.click_element((By.ID, "btn-login"))

    # Book Appointments
    FACILITY_DROPDOWN = (By.ID, "combo_facility")
    HEALTHCARE_CHECKBOX = (By.NAME, "programs")
    VISIT_DATE_INPUT = (By.ID, "txt_visit_date")
    COMMENT_INPUT = (By.ID, "txt_comment")
    BOOK_BUTTON = (By.ID, "btn-book-appointment")

    def fill_appointment_form(self, facility, healthcare, visit_date, comment):
        # Select Facility
        self.find_element(By.ID, "combo_facility").send_keys(facility)
        
        # Select Healthcare Program
        healthcare_options = {"Medicare": 0, "Medicaid": 1, "None": 2}
        self.driver.find_elements(*self.HEALTHCARE_CHECKBOX)[healthcare_options[healthcare]].click()
        
        # Enter Visit Date
        self.enter_text(*self.VISIT_DATE_INPUT, visit_date)

        # Enter Comment
        self.enter_text(*self.COMMENT_INPUT, comment)

    def book_appointment(self):
        self.click_element(*self.BOOK_BUTTON)
