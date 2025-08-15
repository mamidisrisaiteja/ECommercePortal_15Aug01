from playwright.sync_api import Page
from pages.base_page import BasePage
from typing import List

class InventoryPage(BasePage):
    """Inventory/Products page object model."""
    
    def __init__(self, page: Page):
        super().__init__(page)
        
        # Locators
        self.products_title = '.title'
        self.sort_dropdown = '[data-test="product_sort_container"]'
        self.product_items = '.inventory_item'
        self.product_names = '.inventory_item_name'
        self.add_to_cart_buttons = '[id^="add-to-cart"]'
        self.cart_icon = '.shopping_cart_link'
        self.cart_badge = '.shopping_cart_badge'
        self.menu_button = '#react-burger-menu-btn'
        self.logout_link = '#logout_sidebar_link'
    
    def is_products_page_displayed(self) -> bool:
        """Check if products page is displayed."""
        return self.assert_text_present("Products")
    
    def verify_products_title(self) -> bool:
        """Verify products title is present."""
        return self.assert_element_visible(self.products_title)
    
    def verify_add_to_cart_buttons(self) -> bool:
        """Verify add to cart buttons are present."""
        return self.assert_text_present("Add to cart")
    
    def get_product_names(self) -> List[str]:
        """Get all product names."""
        self.wait_for_element(self.product_names)
        product_elements = self.page.locator(self.product_names).all()
        return [element.text_content() for element in product_elements]
    
    def click_sort_dropdown(self) -> bool:
        """Click sort dropdown."""
        return self.click_element(self.sort_dropdown)
    
    def select_sort_option(self, option_text: str) -> bool:
        """Select sort option by text."""
        self.logger.step(f"Selecting sort option: {option_text}")
        if self.click_sort_dropdown():
            option_selector = f'option:has-text("{option_text}")'
            return self.click_element(option_selector)
        return False
    
    def sort_products_by_name_asc(self) -> bool:
        """Sort products by name A to Z."""
        return self.select_sort_option("Name (A to Z)")
    
    def verify_products_sorted_alphabetically(self) -> bool:
        """Verify products are sorted alphabetically."""
        product_names = self.get_product_names()
        sorted_names = sorted(product_names)
        is_sorted = product_names == sorted_names
        
        if is_sorted:
            self.logger.step("Products are correctly sorted alphabetically")
        else:
            self.logger.error(f"Products not sorted. Current: {product_names}, Expected: {sorted_names}")
        
        return is_sorted
    
    def add_first_product_to_cart(self) -> bool:
        """Add first product to cart."""
        first_add_button = f"{self.add_to_cart_buttons}:first-child"
        return self.click_element(first_add_button)
    
    def add_product_to_cart_by_name(self, product_name: str) -> bool:
        """Add specific product to cart by name."""
        product_selector = f'.inventory_item:has-text("{product_name}") {self.add_to_cart_buttons}'
        return self.click_element(product_selector)
    
    def click_cart_icon(self) -> bool:
        """Click cart icon."""
        return self.click_element(self.cart_icon)
    
    def get_cart_items_count(self) -> int:
        """Get number of items in cart."""
        if self.is_element_visible(self.cart_badge):
            count_text = self.get_element_text(self.cart_badge)
            return int(count_text) if count_text.isdigit() else 0
        return 0
    
    def open_menu(self) -> bool:
        """Open hamburger menu."""
        return self.click_element(self.menu_button)
    
    def logout(self) -> bool:
        """Logout from application."""
        if self.open_menu():
            self.wait_for_element(self.logout_link)
            return self.click_element(self.logout_link)
        return False
