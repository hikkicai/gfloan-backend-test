Feature: Calculator restful API test

  Scenario: Verify that app is up and running
    Given url 'http://127.0.0.1:5000/'
    When method get
    Then status 200
    And match response == 'Calculator is up and running!'

  Scenario: Verify that user gets no record before calculation
    Given url 'http://127.0.0.1:5000/get-task/'
    When method get
    Then status 200
    And match response == {times: 0, sum: null }

  Scenario: Verify that calculator adds 2 numbers correctly
    Given url 'http://127.0.0.1:5000/add-task/'
    And request { num1: 2.45 , num2: 5.52 }
    When method post
    Then status 200
    And match response == {result: 7.97}

  Scenario: Verify that missing argument in request
    Given url 'http://127.0.0.1:5000/add-task/'
    And request { num1: 2 }
    When method post
    Then status 400

  Scenario: Verify that invalid request is sent
    Given url 'http://127.0.0.1:5000/add-task/'
    And request { num1: 2 , num2: test }
    When method post
    Then status 400

  Scenario: Verify that user gets calculation times and sum correctly after first calculation
    Given url 'http://127.0.0.1:5000/get-task/'
    When method get
    Then status 200
    And match response == {times: 1, sum: 7.97}

  Scenario: Verify that calculator calculates 3 numbers correctly
    Given url 'http://127.0.0.1:5000/add-task-enhance/'
    And request { num1: 2 , operator1: "+" , num2: 5 , operator2: "-" , num3: 9 }
    When method post
    Then status 200
    And match response == {result: -2 }

  Scenario: Verify invalid number input
    Given url 'http://127.0.0.1:5000/add-task-enhance/'
    And request { num1: 2.5 , operator1: + , num2: 5 , operator2: - , num3: 10 }
    When method post
    Then status 400

  Scenario: Verify invalid operator input
    Given url 'http://127.0.0.1:5000/add-task-enhance/'
    And request { num1: 2 , operator1: * , num2: 5 , operator2: - , num3: 9 }
    When method post
    Then status 400

  Scenario: Verify that user gets calculation times and sum correctly after second calculation
    Given url 'http://127.0.0.1:5000/get-task/'
    When method get
    Then status 200
    And match response == {times: 2, sum: 5.97}