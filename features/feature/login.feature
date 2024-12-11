Feature: Login to CURA Healthcare Service
  As a user
  I want to log in to CURA Healthcare
  So that I can access the application

  @login
  Scenario: Successful login
    Given the user opens the CURA Healthcare website
    When the user logs in with username "John Doe" and password "ThisIsNotAPassword"
    Then the home page is displayed