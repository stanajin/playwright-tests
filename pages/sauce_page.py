from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    # 1. Launch a browser (headed=True lets you see it happen)
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()

    # 2. Go to a website
    page.goto("https://www.saucedemo.com/")

    # 3. Interact with the page
    page.fill("#user-name", "standard_user")
    page.fill("#password", "secret_sauce")
    page.click("#login-button")

    # 4. Take a screenshot of the result
    page.screenshot(path="login_success.png")
    
    browser.close()