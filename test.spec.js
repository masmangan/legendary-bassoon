const { test, expect } = require('@playwright/test');

function randomString(length) {
  return Math.random().toString(36).substring(2, 2 + length);
}

test('Edit personal details test', async ({ page }) => {
  await page.goto('https://opensource-demo.orangehrmlive.com/web/index.php/auth/login');

  await page.getByPlaceholder('Username').fill('Admin');
  await page.getByPlaceholder('Password').fill('admin123');
  await page.getByRole('button', { name: 'Login' }).click();

  await page.getByRole('link', { name: 'My Info' }).click();

  await expect(page.getByPlaceholder('First Name')).toBeVisible();

  await page.getByPlaceholder('First Name').clear();
  await page.getByPlaceholder('First Name').type(randomString(5));

  await page.getByPlaceholder('Middle Name').clear();
  await page.getByPlaceholder('Middle Name').type(randomString(2));
  
  await page.getByPlaceholder('Last Name').clear();
  await page.getByPlaceholder('Last Name').type(randomString(6));

  await page.locator('div.oxd-input-group:has(label:text("Driver\'s License Number"))').locator('input').fill(`BR${Math.floor(Math.random() * 1000)}`);
  await page.locator('div.oxd-input-group:has(label:text("License Expiry Date"))').locator('input').fill('2035-12-10'); // YYYY-DD-MM
  
  const personalForm = page.locator('form:has(input[name="firstName"])');
  await personalForm.getByRole('button', { name: 'Save' }).click();
  await expect(page.locator('.oxd-toast', { hasText: 'Successfully Updated' })).toBeVisible();
});