from playwright.sync_api import Page, expect

class GooglePage:
    def __init__(self, page: Page):
        self.page = page
        self.search_input = page.locator('textarea[name="q"]')

    def goto(self):
        # Base URL will be handled by pytest-playwright base_url fixture or env vars
        self.page.goto("/")

    def verify_title(self):
        expect(self.page).to_have_title("Google")

    def search(self, query: str):
        self.search_input.fill(query)
        self.search_input.press("Enter")

if __name__ == "__main__":
    from playwright.sync_api import sync_playwright
    import time

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context(base_url="https://google.com")
        page = context.new_page()
        google_page = GooglePage(page)
        google_page.goto()
        google_page.verify_title()
        google_page.search("Playwright")
        print("Search performed successfully!")
        time.sleep(2) # Keep browser open briefly
        browser.close()
