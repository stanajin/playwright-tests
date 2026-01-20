from playwright.sync_api import Page, expect
from pages.rahul_shetty_page import RahulShettyLoginPage

def test_login_flow(page: Page):
    """Test login flow using Page Object Model."""
    login_page = RahulShettyLoginPage(page)
    
    # 1. Navigate
    login_page.navigate()
    
    # 2. Perform Login Actions
    # Note: User previously clicked specific elements. We encapsulate this in the POM.
    # Replicating user steps: fill user/pass, select 'teach', click terms link (optional but in user script), check terms, sign in.
    
    # Using the POM granularly or valid login helper:
    login_page.username_input.fill("rahulshettyacademy")
    login_page.password_input.fill("learning")
    login_page.user_type_dropdown.select_option("teach")
    
    # User clicked terms link, then checkbox.
    login_page.terms_link.click()
    login_page.terms_checkbox.check()
    
    login_page.sign_in_button.click()
    
    # 3. Optimize: Replaced time.sleep(5) with explicit expectation
    # Assuming successful login redirects or shows a specific element. 
    # Since we don't know the exact next page element, we can wait for URL change or a broad element.
    # For now, to keep it 'optimized' but safe, we can expect the title to change or URL to change.
    # Or just wait for the button to disappear.
    expect(login_page.sign_in_button).not_to_be_visible()
    # Alternatively check for next page title if known, e.g. "ProtoCommerce"
    # expect(page).to_have_title("ProtoCommerce") 
