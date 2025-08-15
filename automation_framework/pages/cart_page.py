from playwright.sync_api import Page
from pages.base_page import BasePage
from typing import List

class CartPage(BasePage):
    """Cart page object model."""
    
    def __init__(self, page: Page):
        super().__init__(page)
        
        # Locators
        self.cart_title = '.title'
        self.cart_items = '.cart_item'
        self.cart_item_names = '.inventory_item_name'
        self.remove_buttons = '[id^="remove"]'
        self.continue_shopping_button = '[data-test="continue-shopping"]'
        self.checkout_button = '[data-test="checkout"]'
        self.cart_quantity = '.cart_quantity'
    
    def is_cart_page_displayed(self) -> bool:
        """Check if cart page is displayed."""
        return self.assert_text_present("Your Cart")
    
    def verify_cart_title(self) -> bool:
        """Verify cart title is present."""
        return self.assert_element_visible(self.cart_title)
    
    def get_cart_items_count(self) -> int:
        """Get number of items in cart."""
        self.wait_for_element(self.cart_items)
        items = self.page.locator(self.cart_items).all()
        return len(items)
    
    def get_cart_item_names(self) -> List[str]:
        """Get names of all items in cart."""
        self.wait_for_element(self.cart_item_names)
        item_elements = self.page.locator(self.cart_item_names).all()
        return [element.text_content() or "" for element in item_elements]
    
    def is_cart_empty(self) -> bool:
        """Check if cart is empty."""
        return self.get_cart_items_count() == 0
    
    def remove_item_from_cart(self, item_name: str) -> bool:
        """Remove specific item from cart."""
        item_selector = f'.cart_item:has-text("{item_name}") {self.remove_buttons}'
        return self.click_element(item_selector)
    
    def remove_first_item_from_cart(self) -> bool:
        """Remove first item from cart."""
        first_remove_button = f"{self.remove_buttons}:first-child"
        return self.click_element(first_remove_button)
    
    def continue_shopping(self) -> bool:
        """Click continue shopping button."""
        return self.click_element(self.continue_shopping_button)
    
    def proceed_to_checkout(self) -> bool:
        """Click checkout button."""
        return self.click_element(self.checkout_button)
    
    def verify_item_in_cart(self, item_name: str) -> bool:
        """Verify specific item is in cart."""
        cart_items = self.get_cart_item_names()
        return item_name in cart_items
    
    def verify_cart_contains_items(self) -> bool:
        """Verify cart contains at least one item."""
        return self.get_cart_items_count() > 0
    
    def clear_cart(self) -> bool:
        """Remove all items from cart."""
        while not self.is_cart_empty():
            if not self.remove_first_item_from_cart():
                return False
        return True
