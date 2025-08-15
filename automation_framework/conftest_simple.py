"""
Simple conftest.py for CI/CD pipeline testing
Provides basic Playwright fixtures that work in headless environments
"""
import pytest
from playwright.sync_api import sync_playwright, Page, Browser, BrowserContext


@pytest.fixture(scope="session")
def playwright():
    """Start Playwright for the test session."""
    with sync_playwright() as p:
        yield p


@pytest.fixture(scope="session") 
def browser(playwright):
    """Launch browser for the test session."""
    browser = playwright.chromium.launch(headless=True)
    yield browser
    browser.close()


@pytest.fixture(scope="function")
def context(browser):
    """Create a new browser context for each test."""
    context = browser.new_context(
        viewport={"width": 1280, "height": 720}
    )
    yield context
    context.close()


@pytest.fixture(scope="function")
def page(context):
    """Create a new page for each test."""
    page = context.new_page()
    yield page
    page.close()
