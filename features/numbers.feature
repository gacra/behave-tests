Feature: add some numbers

  Scenario: check if a integer is a integer
    When I check if a integer is a integer
    Then It should return "True"

  Scenario: check if a float is a integer
    When I check if a float is a integer
    Then It should return "False"