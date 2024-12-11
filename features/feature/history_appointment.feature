Feature: Appointment History
    As a user
    I want to create an appointment history 
    So that I can get more information

    Background:
        Given I am logged in as a user as history  

    @history
    Scenario: Viewing appointment history
        When The user login in with username "John Doe" and password "ThisIsNotAPassword" as history 
        And the user navigates to "History"
        Then the appointment history is displayed