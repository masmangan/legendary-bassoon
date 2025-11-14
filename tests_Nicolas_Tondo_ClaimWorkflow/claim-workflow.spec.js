const { test, expect } = require('@playwright/test');

test.describe('Claim Workflow Test', () => {
    const url = 'https://opensource-demo.orangehrmlive.com/web/index.php/auth/login';
    const ADMIN_USERNAME = 'Admin';
    const ADMIN_PASSWORD = 'admin123';

    const remarksText = `Automated Claim ${Date.now()}`;

    test.beforeEach(async ({ page }) => {
        await page.goto(url);
        await page.getByPlaceholder('Username').fill(ADMIN_USERNAME);
        await page.getByPlaceholder('Password').fill(ADMIN_PASSWORD);
        await page.getByRole('button', { name: 'Login' }).click();
        await page.getByRole('heading', { name: 'Dashboard' }).waitFor({ timeout: 30000 });
    });

    test('Create a single claim including mandatory fields and verify', async ({ page }) => {
        const claimLink = page.getByRole('link', { name: 'Claim' });
        await claimLink.waitFor({ timeout: 30000 });
        await claimLink.click();

        const employeeClaimsHeading = page.getByRole('heading', { name: 'Employee Claims' });
        await employeeClaimsHeading.waitFor({ timeout: 30000 });

        const submitClaimLink = page.getByRole('link', { name: 'Submit Claim' });
        await submitClaimLink.waitFor({ timeout: 30000 });
        await submitClaimLink.click();

        await page.getByRole('heading', { name: 'Create Claim Request' }).waitFor({ timeout: 30000 });

        const eventDropdown = page.locator('div.oxd-select-text').nth(0);
        await eventDropdown.click();
        await page.getByRole('option').nth(1).click();

        const currencyDropdown = page.locator('div.oxd-select-text').nth(1);
        await currencyDropdown.click();
        await page.getByRole('option').nth(1).click();

        await page.locator('textarea').fill(remarksText);

        await page.getByRole('button', { name: 'Create' }).click();

        const successToast = page.locator('.oxd-toast-content--success');
        await successToast.waitFor({ timeout: 30000 });
        await expect(successToast).toContainText('Successfully Saved');

        const myClaimsLink = page.getByRole('link', { name: 'My Claims' });
        await myClaimsLink.click();
        const createdRow = page.locator('.oxd-table-card').filter({ hasText: remarksText });
        await expect(createdRow).toBeVisible({ timeout: 30000 });
    });
});
