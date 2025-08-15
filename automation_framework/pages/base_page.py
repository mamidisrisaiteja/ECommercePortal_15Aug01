from playwright.sync_api import Page
from utils.helper_utils import HelperUtils
from utils.logger import Logger

class BasePage:
    """Base page class with common functionality."""
    
    def __init__(self, page: Page):
        self.page = page
        self.helper = HelperUtils()
        self.logger = Logger()
    
    def navigate_to(self, url: str):
        """Navigate to specified URL."""
        self.logger.step(f"Navigating to: {url}")
        self.page.goto(url)
        self.helper.wait_for_page_load(self.page)
    
    def get_page_title(self) -> str:
        """Get current page title."""
        return self.page.title()
    
    def get_current_url(self) -> str:
        """Get current page URL."""
        return self.page.url
    
    def wait_for_element(self, selector: str, timeout: int = 30000) -> bool:
        """Wait for element to be visible."""
        return self.helper.wait_for_element(self.page, selector, timeout)
    
    def click_element(self, selector: str, timeout: int = 30000) -> bool:
        """Click an element."""
        self.logger.step(f"Clicking element: {selector}")
        return self.helper.safe_click(self.page, selector, timeout)
    
    def fill_input(self, selector: str, value: str, timeout: int = 30000) -> bool:
        """Fill an input field."""
        self.logger.step(f"Filling input {selector} with value: {value}")
        return self.helper.safe_fill(self.page, selector, value, timeout)
    
    def get_element_text(self, selector: str, timeout: int = 30000) -> str:
        """Get text content of an element."""
        return self.helper.get_text(self.page, selector, timeout) or ""
    
    def is_element_visible(self, selector: str) -> bool:
        """Check if element is visible."""
        return self.helper.is_element_visible(self.page, selector)
    
    def assert_text_present(self, text: str, timeout: int = 30000) -> bool:
        """Assert text is present on the page."""
        self.logger.step(f"Verifying text is present: {text}")
        return self.helper.assert_text_visible(self.page, text, timeout)
    
    def assert_element_visible(self, selector: str, timeout: int = 30000) -> bool:
        """Assert element is visible."""
        self.logger.step(f"Verifying element is visible: {selector}")
        return self.helper.assert_element_visible(self.page, selector, timeout)
    
    def take_screenshot(self, name: str = "screenshot") -> str:
        """Take screenshot."""
        return self.helper.take_screenshot(self.page, name)
    
    def scroll_to_element(self, selector: str):
        """Scroll to element."""
        self.helper.scroll_to_element(self.page, selector)
