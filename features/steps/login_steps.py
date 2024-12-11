# behave feature\login.feature --tags=login
# behave feature\login.feature
import sys
import os
# Path Success
sys.path.append('../') # cara ini berhasil untuk import file di dalam folder
# sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../'))) # cara ini berhasil untuk import file di dalam folder

from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from pages.login_page import LoginPage

@given(u'the user opens the CURA Healthcare website')
def step_impl(context):
    # print(NotImplementedError(u'STEP: Given the user opens the CURA Healthcare website'))
    context.driver = webdriver.Chrome()
    context.page = LoginPage(context.driver)
    context.page.navigate()


@when(u'the user logs in with username "{username}" and password "{password}"')
def step_impl(context, username, password):
    # print(NotImplementedError(u'STEP: When the user logs in with username "John Doe" and password "ThisIsNotAPassword"'))
    context.page.click_login()
    context.page.perform_login(username, password)

@then(u'the home page is displayed')
def step_impl(context):
    # print(NotImplementedError(u'STEP: Then the home page is displayed'))
    assert "Make Appointment" in context.driver.find_element(By.XPATH, "//h2[normalize-space()='Make Appointment']").text
    context.driver.quit()