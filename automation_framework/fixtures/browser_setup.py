from playwright.sync_api import Playwright, Browser, sync_playwright
from typing import Optional


class BrowserSetup:
    """Browser setup and management utilities."""

    @staticmethod
    def get_playwright():
        """Get Playwright instance."""
        return sync_playwright()

    @staticmethod
    def launch_browser(
        playwright: Playwright,
        browser_type: str = "chromium",
        headless: bool = False
    ) -> Browser:
        """Launch browser based on type."""
        browser_options = {
            "headless": headless,
            "args": [
                "--start-maximized",
                "--disable-web-security",
                "--disable-features=VizDisplayCompositor"
            ]
        }

        if browser_type.lower() == "chromium":
            return playwright.chromium.launch(**browser_options)
        elif browser_type.lower() == "firefox":
            return playwright.firefox.launch(**browser_options)
        elif browser_type.lower() == "webkit":
            return playwright.webkit.launch(**browser_options)
        else:
            raise ValueError(f"Unsupported browser type: {browser_type}")

    @staticmethod
    def create_context_with_options(browser: Browser, **kwargs):
        """Create browser context with custom options."""
        user_agent = (
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
            "AppleWebKit/537.36 (KHTML, like Gecko) "
            "Chrome/91.0.4472.124 Safari/537.36"
        )
        default_options = {
            "viewport": {"width": 1920, "height": 1080},
            "ignore_https_errors": True,
            "user_agent": user_agent
        }
        default_options.update(kwargs)
        return browser.new_context(**default_options)