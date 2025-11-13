const { test, expect } = require('@playwright/test');

test('Search for a user in the Admin panel', async ({ page }) => {
  await page.goto('https://opensource-demo.orangehrmlive.com/web/index.php/auth/login');
  await page.getByPlaceholder('Username').fill('Admin');
  await page.getByPlaceholder('Password').fill('admin123');
  await page.getByRole('button', { name: 'Login' }).click();
  await page.getByRole('link', { name: 'Admin' }).click();
  await expect(page.getByRole('heading', { name: 'User Management' })).toBeVisible();
  await page.locator('div.oxd-input-group:has(label:text("Username"))').locator('input').fill('Admin');
  await page.getByRole('button', { name: 'Search' }).click();
  await expect(page.locator('.orangehrm-horizontal-padding', { hasText: 'Record Found' })).toBeVisible();
  const firstResultCell = page.locator('.oxd-table-body .oxd-table-row').first().locator('.oxd-table-cell').nth(1);
  await expect(firstResultCell).toHaveText('Admin');
});