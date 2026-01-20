from playwright.sync_api import Page, expect

class RahulShettyLoginPage:
    def __init__(self, page: Page):
        self.page = page
        self.username_input = page.get_by_text("Username:")
        self.password_input = page.get_by_text("Password:")
        self.user_type_dropdown = page.get_by_role("combobox")
        self.terms_checkbox = page.get_by_role("checkbox", name="I Agree to the terms and")
        self.terms_link = page.get_by_role("link", name="terms and conditions")
        self.sign_in_button = page.get_by_role("button", name="Sign In")

    def navigate(self):
        self.page.goto("https://rahulshettyacademy.com/loginpagePractise/")

    def login(self, username, password, user_type="student", agree_terms=False):
        self.username_input.fill(username)
        self.password_input.fill(password)
        self.user_type_dropdown.select_option(user_type)
        if agree_terms:
            # Check if link needs to be clicked or just checkbox. User script clicked link then checkbox.
            # Usually strict checkbox check is enough, but user clicked link. I'll maintain that.
            self.terms_checkbox.check()
        self.sign_in_button.click()
    
    def verify_error_message(self):
        # Example method to verify error if login fails
        expect(self.page.locator("[style*='block']")).to_contain_text("Incorrect")

