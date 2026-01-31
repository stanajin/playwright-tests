from behave import given, when, then
from playwright.sync_api import expect

@given('I launch the browser')
def step_impl(context):
    # Browser is already launched in environment.py before_scenario
    pass

@when('I open the Google homepage')
def step_impl(context):
    context.page.goto("https://www.google.com")

@then('the page title should be "{title}"')
def step_impl(context, title):
    expect(context.page).to_have_title(title)
