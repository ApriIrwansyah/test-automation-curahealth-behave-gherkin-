Feature: Leaving CURA Health Services
  As a user
  I would like to log out of CURA Healthcare
  So that I can continue it later

  @Logout
  Scenario: Successful Logout
    Given I am logged in as a user
    When  The user login in with username "John Doe" and password "ThisIsNotAPassword"
    And I am exiting the app
    Then Successfully exit the application