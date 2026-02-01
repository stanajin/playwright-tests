from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class BaseSeleniumPage:
    """
    Base class for all Selenium Page Objects.
    Provides common methods for interacting with web elements.
    """
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def find_element(self, locator):
        """Find an element and wait for it to be present."""
        return self.wait.until(EC.presence_of_element_id_located(locator))

    def click(self, locator):
        """Wait for element to be clickable and click it."""
        element = self.wait.until(EC.element_to_be_clickable(locator))
        element.click()

    def enter_text(self, locator, text):
        """Wait for element to be visible, clear it, and enter text."""
        element = self.wait.until(EC.visibility_of_element_located(locator))
        element.clear()
        element.send_keys(text)

    def get_text(self, locator):
        """Wait for element to be visible and return its text."""
        element = self.wait.until(EC.visibility_of_element_located(locator))
        return element.text

    def is_visible(self, locator):
        """Check if an element is visible."""
        try:
            self.wait.until(EC.visibility_of_element_located(locator))
            return True
        except:
            return False

    def scroll_to_element(self, locator):
        """Scroll the page to the specified element."""
        element = self.find_element(locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
