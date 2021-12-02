Feature: Outlook Login
  Scenario: Navigate to Outlook and login
     Given  chrome is launched
    When we navigate to Rediff website
    And we enter username "amalabk@gmail.com" password "amala"
    And we press the login button
    Then we successfully navigate tologin incorrect page
