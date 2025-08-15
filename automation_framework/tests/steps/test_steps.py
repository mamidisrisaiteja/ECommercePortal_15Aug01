import pytest
from pytest_bdd import scenarios, given, when, then, parsers
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from fixtures.test_data import TestData

# Load scenarios from feature files
scenarios('../features/authentication.feature')
scenarios('../features/inventory.feature')
scenarios('../features/cart.feature')

@pytest.fixture
def login_page(page):
    """Login page fixture."""
    return LoginPage(page)

@pytest.fixture
def inventory_page(page):
    """Inventory page fixture."""
    return InventoryPage(page)

@pytest.fixture
def cart_page(page):
    """Cart page fixture."""
    return CartPage(page)

@pytest.fixture
def test_data_fixture():
    """Test data fixture."""
    return TestData()

# Common step definitions

@given('user is on Login Page')
def user_is_on_login_page(login_page, test_data_fixture):
    """Navigate to login page."""
    login_url = test_data_fixture.get_url('login_url')
    login_page.navigate_to_login_page(login_url)
    assert login_page.is_login_page_displayed(), "Login page is not displayed"

@when(parsers.parse('user enters user name as "{username}" and password as "{password}"'))
def user_enters_credentials(login_page, username, password):
    """Enter login credentials."""
    assert login_page.enter_username(username), f"Failed to enter username: {username}"
    assert login_page.enter_password(password), f"Failed to enter password"

@when('click Login Button')
def click_login_button(login_page):
    """Click login button."""
    assert login_page.click_login_button(), "Failed to click login button"

@then(parsers.parse('verify page has text "{text}"'))
def verify_page_has_text(page, text):
    """Verify page contains specific text."""
    from pages.base_page import BasePage
    base_page = BasePage(page)
    assert base_page.assert_text_present(text), f"Text '{text}' not found on page"

@then('Login Button should be still displayed')
def verify_login_button_displayed(login_page):
    """Verify login button is still displayed."""
    assert login_page.is_login_page_displayed(), "Login button is not displayed"

@when('click Sort Icon')
def click_sort_icon(inventory_page):
    """Click sort dropdown."""
    assert inventory_page.click_sort_dropdown(), "Failed to click sort dropdown"

@when('click Sort the Products by Name A–Z')
def sort_products_by_name_asc(inventory_page):
    """Sort products by name A to Z."""
    assert inventory_page.sort_products_by_name_asc(), "Failed to sort products by name"

@then('all the products must be sorted from A to Z')
def verify_products_sorted_alphabetically(inventory_page):
    """Verify products are sorted alphabetically."""
    assert inventory_page.verify_products_sorted_alphabetically(), "Products are not sorted alphabetically"

@when('click Add to cart')
def click_add_to_cart(inventory_page):
    """Add first product to cart."""
    assert inventory_page.add_first_product_to_cart(), "Failed to add product to cart"

@when('click cart icon')
def click_cart_icon(inventory_page):
    """Click cart icon."""
    assert inventory_page.click_cart_icon(), "Failed to click cart icon"

@then('Cart page displays selected items')
def verify_cart_has_items(cart_page):
    """Verify cart contains items."""
    assert cart_page.verify_cart_contains_items(), "Cart does not contain any items"
