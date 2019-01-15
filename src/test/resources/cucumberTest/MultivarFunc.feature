Feature: Multivariate Function

  Scenario Outline: Test Multivariate Function Calculation
    Given i input "<x>" and "<y>"
    When the function is run
    Then the output should be "<result>"

    Examples:
    | x | y | result |
    | 5 | 5 | true   |
    |4.5|3.5| true   |
    | 4 |5.0| false  |
    |5.0| 7 | false  |
    |-1 |-8 | false  |
