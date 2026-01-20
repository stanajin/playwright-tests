"""
Accessibility tests using axe-core
"""
from playwright.sync_api import Page


def test_google_accessibility(page: Page, axe):
    """Test Google homepage for accessibility violations"""
    page.goto("https://google.com")
    
    # Run accessibility scan
    results = axe.run()
    
    # Assert no violations
    assert len(results.violations) == 0, f"Found {len(results.violations)} accessibility violations"


def test_playwright_dev_accessibility(page: Page, axe):
    """Test Playwright.dev homepage for accessibility violations"""
    page.goto("https://playwright.dev")
    
    # Run accessibility scan
    results = axe.run()
    
    # Print violations if any (for debugging)
    if results.violations:
        print(f"\nFound {len(results.violations)} accessibility violations:")
        for violation in results.violations:
            print(f"  - {violation['id']}: {violation['description']}")
            print(f"    Impact: {violation['impact']}")
            print(f"    Help: {violation['helpUrl']}")
    
    # You can choose to fail or just warn
    # For now, let's just assert
    assert len(results.violations) == 0, f"Found {len(results.violations)} accessibility violations"
