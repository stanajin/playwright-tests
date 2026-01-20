"""
Accessibility tests using Playwright's built-in accessibility features
"""
from playwright.sync_api import Page
import json


def test_timesofindia_accessibility_tree(page: Page):
    """Test Times of India homepage accessibility tree"""
    page.goto("https://timesofindia.com", wait_until="domcontentloaded")
    
    # Get accessibility snapshot
    snapshot = page.accessibility.snapshot()
    
    print(f"\n{'='*60}")
    print("Accessibility Tree for Times of India:")
    print(f"{'='*60}")
    print(json.dumps(snapshot, indent=2)[:500])  # Print first 500 chars
    print("\n✅ Accessibility tree captured successfully!")


def test_google_accessibility_tree(page: Page):
    """Test Google homepage accessibility tree"""
    page.goto("https://google.com")
    
    # Get accessibility snapshot
    snapshot = page.accessibility.snapshot()
    
    print(f"\n{'='*60}")
    print("Accessibility Tree for Google:")
    print(f"{'='*60}")
    print(json.dumps(snapshot, indent=2)[:500])  # Print first 500 chars
    print("\n✅ Accessibility tree captured successfully!")


def test_check_aria_labels(page: Page):
    """Example test to check for missing ARIA labels on buttons"""
    page.goto("https://timesofindia.com", wait_until="domcontentloaded")
    
    # Find all buttons
    buttons = page.locator("button").all()
    
    missing_labels = []
    for i, button in enumerate(buttons[:10]):  # Check first 10 buttons
        try:
            aria_label = button.get_attribute("aria-label")
            text = button.inner_text()
            
            if not aria_label and not text:
                missing_labels.append(f"Button {i}")
        except:
            pass
    
    if missing_labels:
        print(f"\n⚠️  Found {len(missing_labels)} buttons without labels:")
        for label in missing_labels:
            print(f"  - {label}")
    else:
        print("\n✅ All checked buttons have proper labels!")
