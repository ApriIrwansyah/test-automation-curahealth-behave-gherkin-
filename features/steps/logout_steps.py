from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from behave import *
from time import sleep 
# behave feature\logout.feature --tags=login
# behave feature\logout.feature

import os
import sys
sys.path.append('../')
from pages.logout_page import LogoutPage
from pages.login_page import LoginPage


@given(u'I am logged in as a user')
def step_impl(context):
    # print(NotImplementedError(u'STEP: Given I am logged in as a user'))
    context.driver = webdriver.Chrome()
    context.page = LoginPage(context.driver)
    context.page.navigate()


@when(u'The user login in with username "{username}" and password "{password}"')
def step_impl(context, username, password):
    # print(NotImplementedError(u'STEP: When The user login in with username "John Doe" and password "ThisIsNotAPassword"')).
    context.page.click_login()
    context.page.perform_login(username, password)


@when(u'I am exiting the app')
def step_impl(context):
    print(NotImplementedError(u'STEP: When I am exiting the app'))
    context.page = LogoutPage(context.driver)
    context.page.navigate_to_logout()


@then(u'Successfully exit the application')
def step_impl(context):
    # print(NotImplementedError(u'STEP: Then Successfully exit the application'))
    assert "CURA Healthcare Service" in context.page.get_logout_success()