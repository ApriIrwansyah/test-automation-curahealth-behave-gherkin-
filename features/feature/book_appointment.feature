Feature: Make an Appointment
  As a user
  I want to make an appointment
  So that I can schedule a visit

  Scenario: Book an appointment successfully
    Given I open the CURA Healthcare Service website
    When I login with username "John Doe" and password "ThisIsNotAPassword"
    And I book an appointment with the following details:
      | facility                  | Hongkong CURA Healthcare Center |
      | apply_for_readmission     | true                            |
      | healthcare_program        | Medicaid                        |
      | visit_date                | 12/15/2024                     |
      | comment                   | Routine checkup                |
    Then I should see the confirmation page
