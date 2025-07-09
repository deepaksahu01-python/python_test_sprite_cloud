Feature: User management verification for reqres

  Scenario: Response for a valid user
    When Get a single user with id 2
    Then Verify user details with firstname as Janet and email as janet.weaver@reqres.in

  Scenario: Create a new user
    When Create a user with name as morpheus and job as leader
    Then Verify user is created

  Scenario: Login without a password
    When Login with username as peter@klaven and without password
    Then User should not be logged in and error message Missing password is sent as response