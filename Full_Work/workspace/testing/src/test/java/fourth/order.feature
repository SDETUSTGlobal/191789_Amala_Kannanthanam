Feature:Orders page
Given user has navigated to orders page
When the user chooses the type of product required
Then the unit price of the product is displayed in the corresponding textbox
When the user enters the quantity of the product required
And clicks the calculate button
Then the total cost is displayed in the corresponding textbox
The user has to enter name,street,city,state,zip as personal information in the corresponding text boxes
The card type is selected as Mastercard
the card number and expiry date is entered
When the process button is clicked
Then the payment is processed
And it is shown that the new order is successfully added
When the reset button is clicked
Then all the data from the columns are erased