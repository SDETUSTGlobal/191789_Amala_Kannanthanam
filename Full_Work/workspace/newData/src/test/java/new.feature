Feature: Login
Background:
Given the user on the login page .
When user follows "Log in"
Scenario: Verification of Login Function 
Given user on the Login Page.
And user enters "username" with "Tester"
And user enters "password" with "test"
And user clicks "login" button 
Then user login should see "Web Orders" title