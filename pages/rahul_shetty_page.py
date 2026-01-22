from playwright.sync_api import Page, expect
from pages.base_page import BasePage


class RahulShettyLoginPage(BasePage):
    """Page object for Rahul Shetty Academy login page."""
    
    def __init__(self, page: Page):
        super().__init__(page)
        # Locators
        self.username_input = page.locator("#username")
        self.password_input = page.locator("#password")
        self.user_type_dropdown = page.get_by_role("combobox")
        self.terms_checkbox = page.locator("#terms")
        self.terms_link = page.get_by_role("link", name="terms and conditions")
        self.sign_in_button = page.locator("#signInBtn")
        self.error_alert = page.locator("[style*='block']")

    def navigate_to_login(self):
        """Navigate to the login page."""
        self.navigate("https://rahulshettyacademy.com/loginpagePractise/")

    def login(self, username: str, password: str, user_type: str = "stud", agree_terms: bool = True):
        """Perform login with given credentials."""
        self.username_input.fill(username)
        self.password_input.fill(password)
        self.user_type_dropdown.select_option(user_type)
        
        if agree_terms:
            self.terms_checkbox.check()
        
        self.sign_in_button.click()
    
    def login_with_terms_link_click(self, username: str, password: str, user_type: str = "teach"):
        """Login flow that includes clicking the terms link before checking the checkbox."""
        self.username_input.fill(username)
        self.password_input.fill(password)
        self.user_type_dropdown.select_option(user_type)
        self.terms_link.click()
        self.terms_checkbox.check()
        self.sign_in_button.click()
    
    def verify_error_message(self, expected_text: str = "Incorrect"):
        """Verify that error message is displayed with expected text."""
        expect(self.error_alert).to_be_visible()
        expect(self.error_alert).to_contain_text(expected_text)
    
    def verify_login_success(self):
        """Verify successful login by checking sign-in button is no longer visible."""
        expect(self.sign_in_button).not_to_be_visible()
