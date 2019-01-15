Feature: Calculator restful API test

  Scenario: Verify that calculator is up and running
    Given url 'http://127.0.0.1:5000/'
    When method get
    Then status 200
    And match //title == 'Calculator'

  Scenario: Verify that calculator adds numbers correctly
    Given url 'http://127.0.0.1:5000/'
    And form field left = 5.62
    And form field right = 6.78
    When method post
    Then status 200
    And match //*[@name="result"]/span == 12.40