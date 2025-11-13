1. Contexto do Projeto

Este teste faz parte das entregas do Trabalho T2 da disciplina Verificação e Validação de Software (PUCRS, 2025/II).

Sistema Alvo: Orange Human Resource Management (Servidor de Demonstração)
Repositório: https://github.com/masmangan/legendary-bassoon

Branch: paygrade-crud-nicolastondo
Autor: Nicolas Tondo

2. Objetivo do Teste

O objetivo deste teste é validar o fluxo completo de gerenciamento de Pay Grades (faixas salariais) dentro do módulo administrativo do sistema.
A jornada cobre as operações de criação, visualização, exclusão e verificação posterior (regressão).

3. Jornada de Usuário Testada

O usuário faz login com credenciais administrativas válidas.

Navega até o menu Admin > Job > Pay Grades.

Cria um novo Pay Grade com nome exclusivo.

Verifica a mensagem de sucesso de criação.

Exclui o Pay Grade recém-criado.

Confirma a mensagem de exclusão bem-sucedida.

Valida que o Pay Grade não aparece mais na lista.

4. Tecnologia Utilizada

Playwright Test (para automação E2E com Node.js)

Execução em navegadores Chromium e headless (modo automático)

Estrutura modular com test.step() para rastreabilidade dos passos

5. Como Instalar e Rodar o Teste
5.1 Pré-requisitos

Node.js (versão 16 ou superior)

npm instalado

5.2 Instalação das Dependências
npm install
npx playwright install

5.3 Execução do Teste

Rode em modo headless:

npx playwright test --grep "Pay Grade" 


Ou modo interativo (com navegador visível):

npx playwright test --grep "Pay Grade" --headed


Para abrir a interface do Playwright:

npx playwright test --ui

6. Declaração de Uso de IA

O código e o README foram elaborados com auxílio técnico da IA ChatGPT (OpenAI), utilizada para revisão e estruturação técnica conforme as práticas de Verificação e Validação de Software.