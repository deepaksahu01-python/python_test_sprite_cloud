#<> Refrence to requirments documents


Feature:Add Sauce Labs products to the shopping cart

@wip
  Scenario: Order Bolt T-shirt using standard_user
    When Log in as standard_user and secret_sauce at https://www.saucedemo.com/
    And Add Bolt T-Shirt to cart
    Then Verify Bolt T-Shirt is listed at the checkout page
  

  Scenario: Checkout an Order Bolt T-shirt
    When Log in as error_user and secret_sauce at https://www.saucedemo.com/
    And Add Bolt T-Shirt to cart
    Then Verify Bolt T-Shirt is listed at the checkout page


  Scenario: Order Bolt T-shirt using locked_user
    When Log in as locked_user and secret_sauce at https://www.saucedemo.com/
    Then User should be successfully logged in
    When Add Bolt T-Shirt to cart
    Then Verify Bolt T-Shirt is listed at the checkout page
