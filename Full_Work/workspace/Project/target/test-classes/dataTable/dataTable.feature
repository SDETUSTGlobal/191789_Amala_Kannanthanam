Feature: Login
Background:
Given the user on the user login page.
When user follows "Log in"
Scenario:Verification of login page
Given  user on Login page.
And user enters "username" with "Tester"
And user enters "pasword" with "test"
And user clicks "login" button
Then the user login should see "Web Orders" title.

