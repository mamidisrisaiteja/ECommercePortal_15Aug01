import logging
import os
from datetime import datetime
from pathlib import Path


class Logger:
    """Logging utility for the test framework."""

    def __init__(self, name: str = "test_automation", level: str = "INFO"):
        self.logger = logging.getLogger(name)
        self.logger.setLevel(getattr(logging, level.upper()))

        # Avoid adding multiple handlers
        if not self.logger.handlers:
            self._setup_handlers()

    def _setup_handlers(self):
        """Setup file and console handlers."""
        # Create logs directory
        logs_dir = Path(__file__).parent.parent / "reports" / "logs"
        logs_dir.mkdir(parents=True, exist_ok=True)

        # File handler
        log_file = logs_dir / f"test_run_{datetime.now().strftime('%Y%m%d_%H%M%S')}.log"
        file_handler = logging.FileHandler(log_file)
        file_handler.setLevel(logging.DEBUG)

        # Console handler
        console_handler = logging.StreamHandler()
        console_handler.setLevel(logging.INFO)

        # Formatter
        formatter = logging.Formatter(
            '%(asctime)s - %(name)s - %(levelname)s - %(funcName)s:%(lineno)d - %(message)s'
        )
        file_handler.setFormatter(formatter)
        console_handler.setFormatter(formatter)

        # Add handlers
        self.logger.addHandler(file_handler)
        self.logger.addHandler(console_handler)

    def info(self, message: str):
        """Log info message."""
        self.logger.info(message)

    def debug(self, message: str):
        """Log debug message."""
        self.logger.debug(message)

    def warning(self, message: str):
        """Log warning message."""
        self.logger.warning(message)

    def error(self, message: str):
        """Log error message."""
        self.logger.error(message)

    def critical(self, message: str):
        """Log critical message."""
        self.logger.critical(message)

    def step(self, message: str):
        """Log test step."""
        self.logger.info(f"STEP: {message}")

    def test_start(self, test_name: str):
        """Log test start."""
        self.logger.info(f"{'='*50}")
        self.logger.info(f"TEST STARTED: {test_name}")
        self.logger.info(f"{'='*50}")

    def test_end(self, test_name: str, status: str):
        """Log test end."""
        self.logger.info(f"TEST ENDED: {test_name} - STATUS: {status}")
        self.logger.info(f"{'='*50}")

    @classmethod
    def get_logger(cls, name: str = "test_automation"):
        """Get logger instance."""
        return cls(name)