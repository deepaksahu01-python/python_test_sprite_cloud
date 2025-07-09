@when(u'Log in as {user_name} and {password} at {url}')
def step_impl(context, user_name, password, url):
    context.products_test.login(url, user_name, password)

@when(u'Add {item} to cart')
def step_impl(context, item):
    context.products_test.add_item_to_cart(item)

@then(u'Verify {item} is listed at the checkout page')
def step_impl(context, item):
    context.products_test.verify_item_at_checkout(item)

@then(u'User should be successfully logged in')
def step_impl(context):
    context.products_test.verify_logging()