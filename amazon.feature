Feature: Login to Amazon e commerce and product purchase

Scenario: Get price, description, and offers for a specific TV

  Given I launch Chrome browser
  When I visit amazon website
  And Amazon homepage is opened successfully

  
  And I log in with valid phone number or email "7019522431" and password "Nisarga@123"
  Then I should login successfully with "<username>"

# When I click on the "SONY 55inch TV"
# Then I should be redirected to the product page

#  When I add the item to the cart
#  Then the item should be added successfully
#
#  When I view the cart
#  Then I should see the "SONY 55inch TV" in the cart
#
#  When I check for offers on the "SONY 55inch TV"
#  Then I should see the current available offer(s)
#
#  When I check the latest 5 reviews for the "SONY 55inch TV"
#  Then I should see the reviews displayed

