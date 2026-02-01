import pytest
from playwright.sync_api import Page, expect
from fixtures.custom_fixtures import sample_user, load_test_data

def test_login_with_fixture(page: Page, sample_user):
    """
    Test that uses the sample_user fixture to perform a login action.
    """
    # Navigate to a site (using SauceDemo as it matches the data)
    page.goto("https://www.saucedemo.com/")
    
    # Use data from the fixture
    username = sample_user['username']
    password = sample_user['password']
    
    print(f"Logging in with user: {username}")
    
    # Perform login
    page.fill("#user-name", username)
    page.fill("#password", password)
    page.click("#login-button")
    
    # Verify login success (checking URL or a specific element)
    expect(page).to_have_url("https://www.saucedemo.com/inventory.html")
