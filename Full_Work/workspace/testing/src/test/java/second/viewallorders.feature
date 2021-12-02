Feature: View all orders Function
To enter into View all orders page
User must be able to access the page once moved to the page
Scenario:View all orders
Given user must be logged in
When User click on view all orders
Then the list of all orders will be displayed in user screen
Scenario: Edit
When user  click on edit
Then edit order page will appear
Then item will be unchecked
Scenario: Check All button
When user click on check button 
Then all items will be checked
Scenario: Uncheck All button
When user click on uncheck button 
Then all items will be unchecked
Scenario: Delete Selected button
When user click on Delete selected button 
Then all the checked items will be deleted