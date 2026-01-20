import pytest
from playwright.sync_api import Page, expect

@pytest.fixture(scope="function", autouse=True)
def before_each_after_each(page: Page):
    print("Running before each test")
    page.goto("https://playwright.dev")
    yield
    print("Running after each test")

def test_has_title(page: Page):
    expect(page).to_have_title("Fast and reliable end-to-end testing for modern web apps | Playwright")