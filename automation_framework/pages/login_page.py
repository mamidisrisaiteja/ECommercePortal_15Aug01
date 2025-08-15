from playwright.sync_api import Page
from pages.base_page import BasePage

class LoginPage(BasePage):
    """Login page object model."""
    
    def __init__(self, page: Page):
        super().__init__(page)
        
        # Locators
        self.username_input = '[data-test="username"]'
        self.password_input = '[data-test="password"]'
        self.login_button = '[data-test="login-button"]'
        self.error_message = '[data-test="error"]'
        self.logo = '.login_logo'
    
    def navigate_to_login_page(self, url: str):
        """Navigate to login page."""
        self.navigate_to(url)
    
    def enter_username(self, username: str) -> bool:
        """Enter username."""
        return self.fill_input(self.username_input, username)
    
    def enter_password(self, password: str) -> bool:
        """Enter password."""
        return self.fill_input(self.password_input, password)
    
    def click_login_button(self) -> bool:
        """Click login button."""
        return self.click_element(self.login_button)
    
    def login(self, username: str, password: str) -> bool:
        """Complete login process."""
        self.logger.step(f"Logging in with username: {username}")
        
        if not self.enter_username(username):
            return False
        if not self.enter_password(password):
            return False
        if not self.click_login_button():
            return False
        
        return True
    
    def is_login_page_displayed(self) -> bool:
        """Check if login page is displayed."""
        return self.is_element_visible(self.login_button)
    
    def get_error_message(self) -> str:
        """Get error message text."""
        return self.get_element_text(self.error_message)
    
    def is_error_message_displayed(self) -> bool:
        """Check if error message is displayed."""
        return self.is_element_visible(self.error_message)
    
    def verify_login_page_elements(self) -> bool:
        """Verify all login page elements are present."""
        elements_present = [
            self.is_element_visible(self.username_input),
            self.is_element_visible(self.password_input),
            self.is_element_visible(self.login_button),
            self.is_element_visible(self.logo)
        ]
        return all(elements_present)
