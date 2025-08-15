import pytest
from playwright.sync_api import Playwright, Browser, BrowserContext, Page
from fixtures.browser_setup import BrowserSetup
from fixtures.test_data import TestData
from utils.config_manager import ConfigManager
from utils.logger import Logger


@pytest.fixture(scope="session")
def config():
    """Load configuration for the test session."""
    return ConfigManager()


@pytest.fixture(scope="session")
def logger():
    """Setup logger for the test session."""
    return Logger()


@pytest.fixture(scope="session")
def playwright_instance(config):
    """Setup Playwright instance for the session."""
    with BrowserSetup.get_playwright() as p:
        yield p


@pytest.fixture(scope="session")
def browser(playwright_instance, config):
    """Setup browser instance for the session."""
    browser = BrowserSetup.launch_browser(
        playwright_instance,
        browser_type=config.get_browser_type(),
        headless=config.is_headless()
    )
    yield browser
    browser.close()


@pytest.fixture(scope="function")
def context(browser, config):
    """Create a new browser context for each test."""
    context = browser.new_context(
        viewport={"width": 1920, "height": 1080},
        record_video_dir="reports/videos/" if config.record_video() else None
    )
    yield context
    context.close()


@pytest.fixture(scope="function")
def page(context):
    """Create a new page for each test."""
    page = context.new_page()
    yield page
    page.close()


@pytest.fixture(scope="session")
def test_data():
    """Load test data for the session."""
    return TestData()


@pytest.fixture(autouse=True)
def setup_test_environment(request, logger):
    """Setup test environment before each test."""
    test_name = request.node.name
    logger.info(f"Starting test: {test_name}")

    yield

    logger.info(f"Completed test: {test_name}")


def pytest_bdd_step_error(
    request, feature, scenario, step, step_func, step_func_args, exception
):
    """Handle BDD step errors."""
    logger = Logger()
    logger.error(f"Step failed: {step['keyword']} {step['name']}")
    logger.error(f"Exception: {str(exception)}")


def pytest_bdd_before_scenario(request, feature, scenario):
    """Hook to run before each scenario."""
    logger = Logger()
    logger.info(f"Starting scenario: {scenario['name']}")


def pytest_bdd_after_scenario(request, feature, scenario):
    """Hook to run after each scenario."""
    logger = Logger()
    logger.info(f"Completed scenario: {scenario['name']}")