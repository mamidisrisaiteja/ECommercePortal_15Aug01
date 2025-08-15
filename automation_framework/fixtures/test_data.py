import json
import yaml
from pathlib import Path
from typing import Dict, Any

class TestData:
    """Test data management utilities."""
    
    def __init__(self):
        self.base_path = Path(__file__).parent.parent
        self._credentials = self._load_credentials()
        self._urls = self._load_urls()
        self._test_data = self._load_test_data()
    
    def _load_credentials(self) -> Dict[str, Any]:
        """Load user credentials."""
        return {
            "valid_user": {
                "username": "standard_user",
                "password": "secret_sauce"
            },
            "invalid_user": {
                "username": "standard_use",
                "password": "secret_sauce"
            },
            "locked_user": {
                "username": "locked_out_user",
                "password": "secret_sauce"
            }
        }
    
    def _load_urls(self) -> Dict[str, str]:
        """Load application URLs."""
        return {
            "base_url": "https://www.saucedemo.com",
            "login_url": "https://www.saucedemo.com/",
            "inventory_url": "https://www.saucedemo.com/inventory.html",
            "cart_url": "https://www.saucedemo.com/cart.html"
        }
    
    def _load_test_data(self) -> Dict[str, Any]:
        """Load general test data."""
        return {
            "expected_texts": {
                "products": "Products",
                "add_to_cart": "Add to cart",
                "your_cart": "Your Cart",
                "login": "Login"
            },
            "sort_options": {
                "name_asc": "Name (A to Z)",
                "name_desc": "Name (Z to A)",
                "price_low_high": "Price (low to high)",
                "price_high_low": "Price (high to low)"
            }
        }
    
    def get_credentials(self, user_type: str) -> Dict[str, str]:
        """Get credentials for specific user type."""
        return self._credentials.get(user_type, {})
    
    def get_url(self, url_type: str) -> str:
        """Get URL for specific type."""
        return self._urls.get(url_type, "")
    
    def get_expected_text(self, text_key: str) -> str:
        """Get expected text for validation."""
        return self._test_data["expected_texts"].get(text_key, "")
    
    def get_sort_option(self, option_key: str) -> str:
        """Get sort option text."""
        return self._test_data["sort_options"].get(option_key, "")
