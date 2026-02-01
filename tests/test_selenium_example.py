import pytest
from pages.selenium_landing_page import SeleniumLandingPage

def test_selenium_google_search(selenium_driver):
    """
    Sample test case using Selenium and POM.
    """
    landing_page = SeleniumLandingPage(selenium_driver)
    
    # Navigate to Google
    landing_page.navigate_to("https://www.google.com")
    
    # Assert title
    assert "Google" in selenium_driver.title
    
    # Search for something
    landing_page.search_for("Selenium Python POM")
    
    # Verify search results page title
    assert "Selenium Python POM" in selenium_driver.title
