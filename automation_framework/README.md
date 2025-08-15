# Test Automation Framework with Playwright MCP Server Integration

## 🚀 Framework Overview

This is a comprehensive Test Automation Framework built using:
- **Python** as the programming language
- **Playwright MCP Server** for browser automation
- **Pytest** as the test runner
- **Cucumber BDD** with pytest-bdd for behavior-driven testing
- **Page Object Model** for maintainable code structure

## 🏗️ Framework Architecture

```
automation_framework/
├── pages/                  # Page Object Model layer
│   ├── base_page.py       # Base page with common functionality
│   ├── login_page.py      # Login page objects and methods
│   ├── inventory_page.py  # Inventory/Products page objects
│   └── cart_page.py       # Shopping cart page objects
├── tests/                  # Test layer
│   ├── features/          # BDD feature files
│   │   ├── authentication.feature  # @auth tagged scenarios
│   │   ├── inventory.feature       # @inventory tagged scenarios
│   │   └── cart.feature           # @cart tagged scenarios
│   └── steps/             # BDD step definitions
│       └── test_steps.py  # Step implementations
├── fixtures/              # Test fixtures layer
│   ├── browser_setup.py   # Browser configuration
│   └── test_data.py       # Test data management
├── utils/                 # Utilities layer
│   ├── config_manager.py  # Configuration management
│   ├── logger.py         # Logging utilities
│   └── helper_utils.py   # Helper functions
├── reports/               # Reports layer
│   ├── screenshots/      # Auto-captured screenshots
│   ├── videos/          # Test execution videos
│   └── logs/            # Execution logs
├── mcp_integration.py     # Playwright MCP integration
├── playwright_mcp_runner.py  # MCP-specific test runner
├── config.yaml           # Framework configuration
├── requirements.txt      # Dependencies
├── pytest.ini           # Pytest configuration
└── conftest.py          # Pytest fixtures
```

## 🎯 Playwright MCP Server Integration

### What is Playwright MCP Server?
The Playwright MCP (Model Context Protocol) server provides a seamless interface for browser automation with enhanced capabilities:

### Key MCP Server Functions Used:
1. **Browser Management**
   - `mcp_playwright_playwright_navigate()` - Navigate to URLs
   - `mcp_playwright_playwright_close()` - Close browser sessions

2. **Element Interactions**
   - `mcp_playwright_playwright_fill()` - Fill input fields
   - `mcp_playwright_playwright_click()` - Click elements
   - `mcp_playwright_playwright_select()` - Select dropdown options

3. **Verification & Debugging**
   - `mcp_playwright_playwright_get_visible_text()` - Extract page text
   - `mcp_playwright_playwright_get_visible_html()` - Get HTML content
   - `mcp_playwright_playwright_screenshot()` - Capture screenshots

4. **Advanced Features**
   - `mcp_playwright_playwright_console_logs()` - Get browser logs
   - `mcp_playwright_playwright_expect_response()` - Monitor network
   - Video recording and file uploads

## 📋 Test Scenarios Implemented

### @auth - Authentication Module
- **TC_AUTH_01**: Login with valid credentials ✅
- **TC_AUTH_02**: Login with invalid credentials ✅

### @inventory - Inventory Module  
- **TC_INV_01**: Verify product listing ✅
- **TC_INV_02**: Sort products by Name (A–Z) ✅

### @cart - Cart Module
- **TC_CART_01**: View cart contents ✅

## 🛠️ Setup Instructions

1. **Install Dependencies**
   ```powershell
   pip install -r requirements.txt
   ```

2. **Install Playwright Browsers**
   ```powershell
   playwright install
   ```

3. **Configure MCP Server** (Already configured in mcp.json)
   ```json
   {
     "servers": {
       "playwright": {
         "command": "npx",
         "args": ["-y", "@executeautomation/playwright-mcp-server"],
         "type": "stdio"
       }
     }
   }
   ```

## 🚀 Running Tests

### Run All Tests
```powershell
pytest tests/
```

### Run by Tags
```powershell
pytest -m auth          # Authentication tests
pytest -m inventory     # Inventory tests  
pytest -m cart          # Cart tests
pytest -m smoke         # Smoke tests
```

### Run with Reports
```powershell
pytest --html=reports/report.html --alluredir=reports/allure-results
```

## 🎥 MCP Server Demo Results

I successfully demonstrated all test scenarios using the Playwright MCP server:

### ✅ Test Results Summary:
- **TC_AUTH_01**: PASSED - Successfully logged in and verified Products page
- **TC_AUTH_02**: PASSED - Login failed as expected with invalid credentials
- **TC_INV_01**: PASSED - Products page displays with Add to cart buttons
- **TC_INV_02**: PASSED - Products sorted alphabetically A to Z
- **TC_CART_01**: PASSED - Cart page displays selected items correctly

### 📸 Screenshots Captured:
- `login_page_initial` - Initial login page
- `products_page_after_login` - Products page after successful login
- `products_sorted_a_to_z` - Products sorted alphabetically
- `cart_page_with_items` - Cart page with selected items
- `login_failed_invalid_credentials` - Failed login attempt

## 🔧 MCP Server Advantages

1. **Real Browser Automation**: Uses actual browser instances (not headless by default)
2. **Visual Feedback**: Automatic screenshot capture for debugging
3. **Cross-Browser Support**: Chromium, Firefox, WebKit
4. **Network Monitoring**: Request/response interception
5. **Console Logs**: Browser console log capture
6. **Element Validation**: Robust element interaction validation
7. **Video Recording**: Optional test execution recording

## 📊 Framework Benefits

- **BDD Approach**: Readable scenarios using Gherkin syntax
- **Page Object Model**: Maintainable and reusable code
- **Modular Design**: Separated concerns (pages, tests, fixtures, utils)
- **Comprehensive Reporting**: HTML, Allure, and custom reports
- **Tag-based Execution**: Run specific test categories
- **Configuration Management**: YAML-based configuration
- **Logging**: Detailed execution logs with timestamps
- **Error Handling**: Robust error handling and recovery

## 🎯 Next Steps

1. **Extend Test Coverage**: Add more test scenarios
2. **CI/CD Integration**: Add pipeline configuration
3. **Database Testing**: Add database validation steps
4. **API Testing**: Integrate API testing capabilities
5. **Performance Testing**: Add performance monitoring
6. **Mobile Testing**: Extend for mobile browsers

This framework demonstrates the power of combining Playwright MCP server with a well-structured BDD framework for comprehensive e-commerce testing.
