const { test, expect } = require('@playwright/test');

test.describe('System Test: Delete Pay Grade Workflow', () => {

    const url = 'https://opensource-demo.orangehrmlive.com/web/index.php/auth/login';
    const ADMIN_USERNAME = 'Admin';
    const ADMIN_PASSWORD = 'admin123';
    const newPayGradeName = `GradeDeleteTest-${Date.now()}`;

    test('Scenario 1: Full Pay Grade system workflow (Create, Delete, Verify)', async ({ page }) => {

        await test.step('1. Login no sistema', async () => {
            await page.goto(url);
            await expect(page.getByPlaceholder('Username')).toBeVisible({ timeout: 10000 });

            await page.getByPlaceholder('Username').fill(ADMIN_USERNAME);
            await page.getByPlaceholder('Password').fill(ADMIN_PASSWORD);
            await page.getByRole('button', { name: 'Login' }).click();

            await page.waitForURL('**/dashboard/index', { timeout: 15000 });
            await expect(page.getByRole('heading', { name: 'Dashboard' })).toBeVisible();
        });

        await test.step('2. Navegação para Admin > Job > Pay Grades', async () => {
            const adminLink = page.locator('a[href="/web/index.php/admin/viewAdminModule"]');
            await expect(adminLink).toBeVisible({ timeout: 10000 });
            await adminLink.click();

            const jobMenu = page.locator('span.oxd-topbar-body-nav-tab-item', { hasText: 'Job' });
            await expect(jobMenu).toBeVisible({ timeout: 10000 });
            await jobMenu.click();

            const payGradesLink = page.locator('a.oxd-topbar-body-nav-tab-link', { hasText: 'Pay Grades' });
            await expect(payGradesLink).toBeVisible({ timeout: 10000 });
            await payGradesLink.click();

            await page.waitForURL('**/viewPayGrades', { timeout: 10000 });
            await expect(page.getByRole('heading', { name: 'Pay Grades' })).toBeVisible();
        });

        await test.step('3. Criação de um novo Pay Grade para exclusão', async () => {
            await expect(page.getByRole('heading', { name: 'Pay Grades' })).toBeVisible({ timeout: 15000 });

            const addButton = page.locator('button', { hasText: /^Add$/ });
            await expect(addButton).toBeEnabled();
            await addButton.click();

            await page.waitForURL('**/savePayGrade', { timeout: 15000 });

            const nameField = page.getByRole('textbox').first();
            await expect(nameField).toBeVisible({ timeout: 10000 });
            await nameField.fill(newPayGradeName);

            const saveButton = page.getByRole('button', { name: 'Save' });
            await expect(saveButton).toBeVisible({ timeout: 10000 });
            await saveButton.click();

            const successToast = page.locator('.oxd-toast-content--success');
            await expect(successToast).toBeVisible({ timeout: 10000 });
            await expect(successToast).toContainText('Successfully Saved');
        });

        await test.step('4. Exclusão do Pay Grade criado', async () => {
            await page.goto('https://opensource-demo.orangehrmlive.com/web/index.php/admin/viewPayGrades');
            await page.waitForSelector('.oxd-table-card', { timeout: 15000 });

            const rowLocator = page.locator('.oxd-table-card').filter({ hasText: newPayGradeName });
            const rowCount = await rowLocator.count();

            if (rowCount === 0) {
                throw new Error(`O Pay Grade "${newPayGradeName}" não foi encontrado na tabela para exclusão.`);
            }

            const deleteButton = rowLocator.locator('i.oxd-icon.bi-trash').first();
            await expect(deleteButton).toBeVisible({ timeout: 10000 });
            await deleteButton.click();

            const confirmModal = page.getByRole('heading', { name: 'Are you Sure?' });
            await expect(confirmModal).toBeVisible({ timeout: 10000 });

            const confirmDeleteButton = page.getByRole('button', { name: 'Yes, Delete' });
            await expect(confirmDeleteButton).toBeVisible({ timeout: 10000 });
            await confirmDeleteButton.click();

            const deleteSuccessToast = page.locator('.oxd-toast-content--success');
            await expect(deleteSuccessToast).toBeVisible({ timeout: 10000 });
            await expect(deleteSuccessToast).toContainText('Successfully Deleted');
        });

        await test.step('5. Verificação de que o Pay Grade não existe mais na lista', async () => {
            await page.goto('https://opensource-demo.orangehrmlive.com/web/index.php/admin/viewPayGrades');
            const deletedGrade = page.locator('.oxd-table-card').filter({ hasText: newPayGradeName });
            await deletedGrade.waitFor({ state: 'detached', timeout: 15000 });
        });
    });
});
