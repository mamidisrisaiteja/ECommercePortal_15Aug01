from playwright.sync_api import Page, expect
from typing import Optional
import time

class HelperUtils:
    """Helper utilities for common test operations."""
    
    @staticmethod
    def wait_for_element(page: Page, selector: str, timeout: int = 30000) -> bool:
        """Wait for element to be visible."""
        try:
            page.wait_for_selector(selector, timeout=timeout)
            return True
        except Exception:
            return False
    
    @staticmethod
    def safe_click(page: Page, selector: str, timeout: int = 30000) -> bool:
        """Safely click an element with wait."""
        try:
            page.wait_for_selector(selector, timeout=timeout)
            page.click(selector)
            return True
        except Exception:
            return False
    
    @staticmethod
    def safe_fill(page: Page, selector: str, value: str, timeout: int = 30000) -> bool:
        """Safely fill an input field."""
        try:
            page.wait_for_selector(selector, timeout=timeout)
            page.fill(selector, value)
            return True
        except Exception:
            return False
    
    @staticmethod
    def get_text(page: Page, selector: str, timeout: int = 30000) -> Optional[str]:
        """Get text content of an element."""
        try:
            page.wait_for_selector(selector, timeout=timeout)
            return page.text_content(selector)
        except Exception:
            return None
    
    @staticmethod
    def is_element_visible(page: Page, selector: str) -> bool:
        """Check if element is visible."""
        try:
            return page.is_visible(selector)
        except Exception:
            return False
    
    @staticmethod
    def scroll_to_element(page: Page, selector: str):
        """Scroll to element."""
        try:
            page.locator(selector).scroll_into_view_if_needed()
        except Exception:
            pass
    
    @staticmethod
    def take_screenshot(page: Page, name: str = "screenshot") -> str:
        """Take screenshot and return path."""
        try:
            timestamp = str(int(time.time()))
            screenshot_path = f"reports/screenshots/{name}_{timestamp}.png"
            page.screenshot(path=screenshot_path)
            return screenshot_path
        except Exception:
            return ""
    
    @staticmethod
    def wait_for_page_load(page: Page, timeout: int = 30000):
        """Wait for page to load completely."""
        try:
            page.wait_for_load_state("networkidle", timeout=timeout)
        except Exception:
            pass
    
    @staticmethod
    def assert_text_visible(page: Page, text: str, timeout: int = 30000) -> bool:
        """Assert that text is visible on the page."""
        try:
            expect(page.get_by_text(text)).to_be_visible(timeout=timeout)
            return True
        except Exception:
            return False
    
    @staticmethod
    def assert_element_visible(page: Page, selector: str, timeout: int = 30000) -> bool:
        """Assert that element is visible."""
        try:
            expect(page.locator(selector)).to_be_visible(timeout=timeout)
            return True
        except Exception:
            return False
