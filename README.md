1. Contexto do Projeto

Este projeto faz parte do Trabalho T2 da disciplina Verificação e Validação de Software (PUCRS, 2025/II) e tem como objetivo automatizar e validar fluxos críticos do sistema Orange Human Resource Management (OrangeHRM).

O foco deste teste é o módulo My Info > Claims, garantindo que a criação e verificação de uma claim funcionem corretamente no perfil do usuário.

Sistema Alvo: OrangeHRM (Servidor de Demonstração)

Repositório: Legendary Bassoon GitHub

Branch utilizada: claim-workflow-nicolastondo

Autor: Nicolas Tondo

2. Objetivo do Teste

Validar o fluxo completo de criação e verificação de Claims, incluindo:

Login com credenciais válidas.

Navegação até My Info > Claims.

Criação de uma nova claim com valor, tipo e descrição únicos.

Verificação da mensagem de sucesso.

Confirmação de que a claim aparece na tabela de registros do usuário.

3. Jornada de Usuário Testada

O teste simula o seguinte comportamento:

Acessar o sistema e realizar login com Admin / admin123.

Navegar até My Info > Claims.

Clicar em Add para criar uma nova claim.

Preencher os campos obrigatórios:

Amount: 1500 (exemplo)

Claim Type: Travel (exemplo)

Comment: descrição única gerada dinamicamente

Clicar em Save / Create.

Verificar o toast de sucesso com a mensagem “Successfully Saved”.

Confirmar que a claim aparece corretamente na tabela de claims.

4. Tecnologias Utilizadas

Playwright Test – automação E2E com Node.js

Navegador Chromium, em modo headless ou headed

Estrutura de testes modular com test.describe e test.step

Validação de elementos via getByRole, getByPlaceholder e locator

5. Instalação e Execução
5.1 Pré-requisitos

Node.js ≥ 16

npm instalado

5.2 Instalação das Dependências
npm install
npx playwright install

5.3 Execução dos Testes

Modo headless (automático):

npx playwright test --grep "Claim Workflow"


Modo interativo (navegador visível):

npx playwright test --grep "Claim Workflow" --headed


Abrir interface do Playwright UI:

npx playwright test --ui

6. Estrutura do Teste

O teste está organizado em dois cenários principais:

Create a single claim including mandatory fields and verify

Cria uma claim com campos obrigatórios preenchidos.

Verifica toast de sucesso e presença da claim na tabela.

Verify access to Assign Claim form via link

Navega até a tela de Assign Claim.

Verifica carregamento correto do formulário e URL.

Exemplo de snippet do teste:

const { test, expect } = require('@playwright/test');

    test.beforeEach(async ({ page }) => {
        await page.goto(url);
        await page.getByPlaceholder('Username').fill(ADMIN_USERNAME);
        await page.getByPlaceholder('Password').fill(ADMIN_PASSWORD);
        await page.getByRole('button', { name: 'Login' }).click();
        await page.waitForURL('**/dashboard/index');
    });

    test('Create a single claim including mandatory fields and verify', async ({ page }) => {
        // Navegação e criação de claim
        await page.getByRole('link', { name: 'Claim' }).click();
        await page.getByRole('link', { name: 'Submit Claim' }).click();
        await page.locator('textarea').fill(remarksText);
        await page.getByRole('button', { name: 'Create' }).click();

        // Validação
        const successToast = page.locator('.oxd-toast-content--success');
        await expect(successToast).toBeVisible({ timeout: 10000 });
        await expect(successToast).toContainText('Successfully Saved');
        await page.getByRole('link', { name: 'My Claims' }).click();
        const createdRow = page.locator('.oxd-table-card').filter({ hasText: remarksText });
        await expect(createdRow).toBeVisible({ timeout: 10000 });
    });
});

7. Declaração de Uso de IA

O código-fonte e este README foram elaborados com auxílio técnico da IA ChatGPT (OpenAI), utilizada para revisão, estruturação e boas práticas de documentação, conforme as diretrizes da disciplina de Verificação e Validação de Software.
