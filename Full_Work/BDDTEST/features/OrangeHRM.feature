Feature: OrangeHRM Logo
  Scenario: Logo presence on orange hrm homepage
    Given launch chrome browser
    When open orange hrm homepage
    Then verify logo is present on the page
    And close browser
