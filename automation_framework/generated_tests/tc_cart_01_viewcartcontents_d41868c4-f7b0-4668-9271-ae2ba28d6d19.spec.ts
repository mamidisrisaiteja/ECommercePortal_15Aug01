
import { test } from '@playwright/test';
import { expect } from '@playwright/test';

test('TC_CART_01_ViewCartContents_2025-08-15', async ({ page, context }) => {
  
    // Navigate to URL
    await page.goto('https://www.saucedemo.com');

    // Fill input field
    await page.fill('[data-test="username"]', 'standard_user');

    // Fill input field
    await page.fill('[data-test="password"]', 'secret_sauce');

    // Click element
    await page.click('[data-test="login-button"]');

    // Click element
    await page.click('[data-test="add-to-cart-sauce-labs-backpack"]');

    // Click element
    await page.click('.btn_inventory:first-child');

    // Click element
    await page.click('.shopping_cart_link');

    // Take screenshot
    await page.screenshot({ path: 'TC_CART_01_your_cart_displayed.png' });
});