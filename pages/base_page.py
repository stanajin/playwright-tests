from playwright.sync_api import Page, expect


class BasePage:
    """Base page class with common functionality for all page objects."""
    
    def __init__(self, page: Page):
        self.page = page
    
    def navigate(self, url: str):
        """Navigate to a specific URL."""
        self.page.goto(url)
    
    def get_title(self) -> str:
        """Get the current page title."""
        return self.page.title()
    
    def wait_for_url(self, url: str, timeout: int = 5000):
        """Wait for URL to match expected value."""
        self.page.wait_for_url(url, timeout=timeout)
    
    def wait_for_element(self, selector: str, timeout: int = 5000):
        """Wait for an element to be visible."""
        self.page.wait_for_selector(selector, state="visible", timeout=timeout)
    
    def is_element_visible(self, selector: str) -> bool:
        """Check if an element is visible."""
        return self.page.locator(selector).is_visible()
