from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from time import sleep
from behave import *

import os 
import sys
sys.path.append('../')
from pages.login_page import LoginPage
from pages.history_page import HistoryAppointment

# behave feature\history_appointment.feature --tags=history
# behave feature\history_appointment.feature


@given(u'I am logged in as a user as history')
def step_impl(context):
    # print(NotImplementedError(u'STEP: Given I am logged in as a user as history'))
    context.driver = webdriver.Chrome()
    context.page = LoginPage(context.driver)
    context.page.navigate()
    

@when(u'The user login in with username "{username}" and password "{password}" as history')
def step_impl(context, username, password):
   #  print(NotImplementedError(u'STEP: When The user login in with username "John Doe" and password "ThisIsNotAPassword" as history'))
    context.page.click_login()
    context.page.perform_login(username, password)
    assert "Make Appointment" in context.driver.find_element(By.XPATH, "//h2[normalize-space()='Make Appointment']").text

@when(u'the user navigates to "History"')
def step_impl(context):
    # print(NotImplementedError(u'STEP: When the user navigates to "History"'))
    context.page = HistoryAppointment(context.driver)
    context.page.navigate_to_history()

@then(u'the appointment history is displayed')
def step_impl(context):
    # print(NotImplementedError(u'STEP: Then the appointment history is displayed'))
    assert "History" in context.page.get_appointment_record()