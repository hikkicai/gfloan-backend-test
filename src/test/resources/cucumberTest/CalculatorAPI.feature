Feature: Calculator restful API test

  Scenario: Verify that app is up and running
    Given url 'http://127.0.0.1:5000/'
    When method get
    Then status 200
    And match //title == 'Calculator'

  Scenario: Verify that app adds 2 numbers correctly
    Given url 'http://127.0.0.1:5000/'
    And form field num1 = 5.62
    And form field num2 = 6.78
    When method post
    Then status 200
    And match //*[@name="result"]/span == 12.40

  Scenario: Verify that app handles invalid input properly
    Given url 'http://127.0.0.1:5000/'
    And form field num1 = 5.62
    And form field num2 = 'abc'
    When method post
    Then status 200
    And match //*[@name="result"]/span == ''
    And match //*[@name="msg"] contains 'Invalid data was given'

  Scenario: Verify that user gets calculation times and sums correctly

  Scenario: Verify that app calculates 3 numbers correctly

  Scenario: Verify that app handles invalid number input

  Scenario: Verify that app handles invalid operator input