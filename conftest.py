import os
import pytest
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

@pytest.fixture(scope="session", autouse=True)
def load_env():
    # This fixture runs before the session starts to ensure env vars are loaded
    # If BASE_URL is set in .env, we can inject it, but pytest-playwright uses pytest.ini or CLI args for base_url usually.
    # However, if we want to override pytest.ini base_url with env var, we can do it here.
    base_url = os.getenv("BASE_URL")
    if base_url:
        os.environ["base_url"] = base_url


@pytest.fixture(scope="session")
def browser_context_args(browser_context_args):
    return {
        **browser_context_args,
        "viewport": {
            "width": 1920,
            "height": 1080,
        }
    }


def pytest_html_report_title(report):
    """Customize the HTML report title"""
    report.title = "Playwright Test Automation Report"


def pytest_configure(config):
    """Add custom environment info to HTML report"""
    if not hasattr(config, '_metadata'):
        config._metadata = {}
    config._metadata["Browsers"] = "Chromium, Firefox, WebKit"
    config._metadata["Test Framework"] = "Playwright + Pytest"

