Feature: Search


  Scenario Outline: Search for a book then bookmark it for reading
    Given User is on 'Goodreads' page
    When User clicks on 'Log In' button at Goodreads page
    Then User enters '<username>' and '<password>'
    And User clicks on 'Log In' button at Login page
    And User searches for a book with '<name_book>'
    And User can mark it for reading

    Examples:
      | username                   | password  | name_book |
      | vuvanthanh.100mm@gmail.com | 123456789 | appium    |