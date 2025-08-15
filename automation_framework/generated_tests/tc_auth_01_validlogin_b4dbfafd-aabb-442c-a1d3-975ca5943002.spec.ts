
import { test } from '@playwright/test';
import { expect } from '@playwright/test';

test('TC_AUTH_01_ValidLogin_2025-08-15', async ({ page, context }) => {
  
    // Navigate to URL
    await page.goto('https://www.saucedemo.com');

    // Fill input field
    await page.fill('[data-test="username"]', 'standard_user');

    // Fill input field
    await page.fill('[data-test="password"]', 'secret_sauce');

    // Click element
    await page.click('[data-test="login-button"]');

    // Take screenshot
    await page.screenshot({ path: 'TC_AUTH_01_products_page_verified.png' });
});