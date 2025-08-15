import yaml
import os
from pathlib import Path
from typing import Any, Dict

class ConfigManager:
    """Configuration management for the test framework."""
    
    def __init__(self, config_file: str = "config.yaml"):
        self.base_path = Path(__file__).parent.parent.parent
        self.config_path = self.base_path / config_file
        self._config = self._load_config()
    
    def _load_config(self) -> Dict[str, Any]:
        """Load configuration from YAML file."""
        try:
            if self.config_path.exists():
                with open(self.config_path, 'r') as file:
                    return yaml.safe_load(file)
            else:
                return self._get_default_config()
        except Exception as e:
            print(f"Error loading config: {e}")
            return self._get_default_config()
    
    def _get_default_config(self) -> Dict[str, Any]:
        """Get default configuration."""
        return {
            "browser": {
                "type": "chromium",
                "headless": False,
                "viewport": {
                    "width": 1920,
                    "height": 1080
                }
            },
            "timeouts": {
                "default": 30000,
                "navigation": 60000,
                "element": 10000
            },
            "reporting": {
                "screenshots": True,
                "videos": False,
                "allure": True
            },
            "urls": {
                "base_url": "https://www.saucedemo.com"
            }
        }
    
    def get_browser_type(self) -> str:
        """Get browser type from config."""
        return self._config.get("browser", {}).get("type", "chromium")
    
    def is_headless(self) -> bool:
        """Check if browser should run in headless mode."""
        return self._config.get("browser", {}).get("headless", False)
    
    def get_viewport(self) -> Dict[str, int]:
        """Get viewport configuration."""
        return self._config.get("browser", {}).get("viewport", {"width": 1920, "height": 1080})
    
    def get_timeout(self, timeout_type: str = "default") -> int:
        """Get timeout value for specific type."""
        return self._config.get("timeouts", {}).get(timeout_type, 30000)
    
    def record_video(self) -> bool:
        """Check if video recording is enabled."""
        return self._config.get("reporting", {}).get("videos", False)
    
    def take_screenshots(self) -> bool:
        """Check if screenshots are enabled."""
        return self._config.get("reporting", {}).get("screenshots", True)
    
    def get_base_url(self) -> str:
        """Get base URL from config."""
        return self._config.get("urls", {}).get("base_url", "https://www.saucedemo.com")
    
    def get_config_value(self, key_path: str, default=None) -> Any:
        """Get configuration value using dot notation (e.g., 'browser.type')."""
        keys = key_path.split('.')
        value = self._config
        
        for key in keys:
            if isinstance(value, dict) and key in value:
                value = value[key]
            else:
                return default
        
        return value
