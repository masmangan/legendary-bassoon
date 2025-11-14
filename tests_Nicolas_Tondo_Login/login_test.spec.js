// Playwright: Teste Funcional Básico de Login (Happy Path)
const { test, expect } = require('@playwright/test');

test.describe('Functional Test: Basic Login Success', () => {
    const url = 'https://opensource-demo.orangehrmlive.com/web/index.php/auth/login';
    const ADMIN_USERNAME = 'Admin';
    const ADMIN_PASSWORD = 'admin123';

    test('Should successfully login with valid credentials', async ({ page }) => {
        await test.step('1. Navegar para a página de Login', async () => {
            await page.goto(url);
            await expect(page.getByRole('heading', { name: 'Login' })).toBeVisible();
        });

        await test.step('2. Preencher credenciais válidas', async () => {
            await page.getByPlaceholder('Username').fill(ADMIN_USERNAME);
            await page.getByPlaceholder('Password').fill(ADMIN_PASSWORD);
        });

        await test.step('3. Clicar no botão Login', async () => {
            await page.getByRole('button', { name: 'Login' }).click();
        });

        await test.step('4. Verificar o redirecionamento para o Dashboard', async () => {
            await page.waitForURL('**/dashboard/index');
            await expect(page.getByRole('heading', { name: 'Dashboard' })).toBeVisible();
        });
    });
});
