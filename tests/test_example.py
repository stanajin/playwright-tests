from pages.google_page import GooglePage

def test_google_search(page):
    google_page = GooglePage(page)
    
    google_page.goto()
    google_page.verify_title()
    google_page.search("Playwright")
