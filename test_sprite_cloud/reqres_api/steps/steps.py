@when(u'Get a single user with id {id}')
def step_impl(context, id):
    context.existing_user = context.user_management_test.get_user(id)

@when(u'Get list of all users')
def step_impl(context, id):
    context.actual_users = context.user_management_test.get_users()

@then(u'Verify user details with firstname as {first_name} and email as {email}')
def step_impl(context, first_name, email):
    expected_user = {'first_name': first_name, 'email': email}
    context.user_management_test.verify_existing_user(context.existing_user, expected_user)

@when(u'Create a user with name as {name} and job as {job}')
def step_impl(context, name, job):
    context.expected_user = {'name': name, 'job': job}
    context.created_user = context.user_management_test.create_user(name, job)


@then(u'Verify user is created')
def step_impl(context):
    context.user_management_test.verify_created_user(context.created_user, context.expected_user)

@when(u'Login with username as {user_name} and without password')
def step_impl(context, user_name):
    context.login_reponse = context.user_management_test.login(user_name)


@then(u'User should not be logged in and error message {error_msg} is sent as response')
def step_impl(context, error_msg):
    context.user_management_test.verify_login(context.login_reponse, error_msg)