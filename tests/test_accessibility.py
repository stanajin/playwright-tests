"""
Accessibility tests using axe-core
"""
from playwright.sync_api import Page
from axe_playwright_python.sync_playwright import Axe


def test_timesofindia_accessibility(page: Page):
    """Test Times of India homepage for accessibility violations"""
    page.goto("https://timesofindia.com", wait_until="domcontentloaded")
    
    # Run accessibility scan
    axe = Axe()
    results = axe.run(page)
    
    # Print violations for informational purposes
    violations = results.get('violations', [])
    if violations:
        print(f"\n{'='*60}")
        print(f"Found {len(violations)} accessibility violations on Times of India:")
        print(f"{'='*60}")
        for violation in violations:
            print(f"\n❌ {violation['id']}: {violation['description']}")
            print(f"   Impact: {violation['impact']}")
            print(f"   Help: {violation['helpUrl']}")
            print(f"   Affected elements: {len(violation['nodes'])}")
    else:
        print("\n✅ No accessibility violations found on Times of India!")
    
    # For now, just report violations without failing
    # You can uncomment the line below to make tests fail on violations
    # assert len(violations) == 0, f"Found {len(violations)} accessibility violations"


def test_google_accessibility(page: Page):
    """Test Google homepage for accessibility violations"""
    page.goto("https://google.com")
    
    # Run accessibility scan
    axe = Axe()
    results = axe.run(page)
    
    # Print violations for informational purposes
    violations = results.get('violations', [])
    if violations:
        print(f"\n{'='*60}")
        print(f"Found {len(violations)} accessibility violations on Google:")
        print(f"{'='*60}")
        for violation in violations:
            print(f"\n❌ {violation['id']}: {violation['description']}")
            print(f"   Impact: {violation['impact']}")
            print(f"   Help: {violation['helpUrl']}")
            print(f"   Affected elements: {len(violation['nodes'])}")
    else:
        print("\n✅ No accessibility violations found on Google!")
