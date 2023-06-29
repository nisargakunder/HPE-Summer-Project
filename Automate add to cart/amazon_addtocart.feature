Feature: Login to Amazon e commerce and product purchase

Scenario Outline: Get price, description, and offers for a specific TV

  Given I launch Chrome browser
  When I visit amazon website
  Then Amazon homepage is opened successfully

  Given I am on the Amazon e-commerce site
  When I log in with valid phone number or email "<mobileno>" and password "<password>"
  Then I should login successfully

  And search for the "SONY 55inch TV"
  And click on search button
  And find the third product
  And fetch price of the product
  And fetch the description of product
  And click add to cart button

  And Displays the offers
    
  And the user navigates to the reviews section
  Then the user should be able to view the reviews

  And close browser

  Examples:
      | mobileno | password |
      |          |          |
  

