from behave import fixture, use_fixture
from playwright.sync_api import sync_playwright

def before_all(context):
    context.playwright = sync_playwright().start()
    # You can launch the browser here if you want a single browser instance for all tests
    # context.browser = context.playwright.chromium.launch(headless=False)

def after_all(context):
    # context.browser.close()
    context.playwright.stop()

def before_scenario(context, scenario):
    # Launch browser for each scenario to ensure clean state, or use a persistent one if preferred
    context.browser = context.playwright.chromium.launch(headless=False) 
    context.context = context.browser.new_context(viewport={"width": 1920, "height": 1080})
    context.page = context.context.new_page()

def after_scenario(context, scenario):
    context.page.close()
    context.context.close()
    context.browser.close()
