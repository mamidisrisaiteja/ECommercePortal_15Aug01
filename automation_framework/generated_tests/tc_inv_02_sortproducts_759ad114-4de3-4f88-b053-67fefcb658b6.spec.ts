
import { test } from '@playwright/test';
import { expect } from '@playwright/test';

test('TC_INV_02_SortProducts_2025-08-15', async ({ page, context }) => {
  
    // Navigate to URL
    await page.goto('https://www.saucedemo.com');

    // Fill input field
    await page.fill('[data-test="username"]', 'standard_user');

    // Fill input field
    await page.fill('[data-test="password"]', 'secret_sauce');

    // Click element
    await page.click('[data-test="login-button"]');

    // Select option
    await page.selectOption('[data-test="product-sort-container"]', 'az');

    // Take screenshot
    await page.screenshot({ path: 'TC_INV_02_products_sorted_a_to_z.png' });
});