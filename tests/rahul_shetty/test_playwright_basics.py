from playwright.sync_api import Page
from pages.rahul_shetty_page import RahulShettyLoginPage
from data.test_data import VALID_USERNAME, VALID_PASSWORD, USER_TYPE_TEACHER


def test_login_flow_with_terms_link(page: Page):
    """Test login flow that includes clicking the terms link before checkbox."""
    login_page = RahulShettyLoginPage(page)
    
    # Navigate to login page
    login_page.navigate_to_login()
    
    # Perform login with terms link click (replicates original user flow)
    login_page.login_with_terms_link_click(VALID_USERNAME, VALID_PASSWORD, USER_TYPE_TEACHER)
    
    # Verify successful login
    login_page.verify_login_success()
