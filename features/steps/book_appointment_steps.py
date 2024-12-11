# behave feature\book_appointment.feature --tags=bookappointment
# behave feature\book_appointment.feature

from behave import *
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from time import sleep
import os
import sys
sys.path.append('../') # cara ini berhasil untuk import file di dalam folder
# sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../'))) # cara ini berhasil untuk import file di dalam folder
from pages.appointment_page import BookingPage


@given(u'I open the CURA Healthcare Service website')
def step_impl(context):
    # print(NotImplementedError(u'STEP: Given I open the CURA Healthcare Service website'))
    context.driver  = webdriver.Chrome()
    context.page    = BookingPage(context.driver)
    context.driver.get("https://katalon-demo-cura.herokuapp.com/")
    context.driver.maximize_window()

@when(u'I login with username "{username}" and password "{password}"')
def step_impl(context, username, password):
    # print(NotImplementedError(u'STEP: When I login with username "John Doe" and password "ThisIsNotAPassword"'))
    context.page.click_login()  # Klik tombol login
    context.page.login(username, password)

@when(u'I book an appointment with the following details')
def step_impl(context):
    # print(NotImplementedError(u'STEP: When I book an appointment with the following details'))
    context.driver.find_element(By.XPATH, "//input[@id='chk_hospotal_readmission']").click()
    sleep(1)
    context.driver.find_element(By.XPATH, "//input[@id='radio_program_medicaid']").click()
    sleep(1)
    context.driver.find_element(By.XPATH, "//input[@id='txt_visit_date']").send_keys('05/12/2024')
    sleep(1)
    context.driver.find_element(By.XPATH, "//textarea[@id='txt_comment']").send_keys('rawat inap')
    sleep(1)
    context.driver.find_element(By.XPATH, "//button[@id='btn-book-appointment']").click()


@then(u'I should see the confirmation page')
def step_impl(context):
    print(NotImplementedError(u'STEP: Then I should see the confirmation page'))
    confirmation_message = context.driver.find_element(By.XPATH, "//h2[normalize-space()='Appointment Confirmation']").text
    assert confirmation_message == "Appointment Confirmation"
    print(confirmation_message)
    context.driver.quit()