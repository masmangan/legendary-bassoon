1. Contexto do Projeto

Este teste faz parte das entregas do Trabalho T2 da disciplina Verificação e Validação de Software (PUCRS, 2025/II).

Sistema Alvo: Orange Human Resource Management (Servidor de Demonstração)
Repositório: https://github.com/masmangan/legendary-bassoon

Branch: login-success
Autor: Nicolas Tondo

2. Objetivo do Teste

O objetivo deste script é validar o fluxo de login com credenciais válidas, garantindo que o usuário "Admin" consiga acessar o painel principal (Dashboard) do sistema Orange HRM.

Este é um teste funcional (E2E), que cobre uma jornada crítica de autenticação.
A execução simula as ações reais de um usuário humano e verifica o comportamento esperado do sistema.

3. Jornada de Usuário Testada

A jornada de usuário validada por este teste é a seguinte:

O usuário acessa a página de login.

O sistema exibe o formulário de autenticação.

O usuário insere credenciais válidas (Admin / admin123).

O usuário clica no botão Login.

O sistema autentica o usuário e redireciona para o Dashboard.

O título "Dashboard" é exibido na tela, confirmando o sucesso da operação.

4. Tecnologia Utilizada

O teste foi desenvolvido com Playwright, uma ferramenta moderna de automação de testes E2E (End-to-End) para Node.js, que oferece suporte a múltiplos navegadores e execução em modo headless ou interativo.

5. Como Instalar e Rodar o Teste
5.1 Pré-requisitos

Node.js (versão 16 ou superior)

npm (gerenciador de pacotes do Node.js)

5.2 Instalação das Dependências
# Clonar o repositório
git clone https://github.com/masmangan/legendary-bassoon.git

# Entrar na branch do seu teste
git checkout login-success

# Instalar dependências
npm install @playwright/test

# Instalar navegadores necessários
npx playwright install

5.3 Execução do Teste

Executar em modo headless (sem abrir o navegador):

npx playwright test


Executar em modo headed (abrindo o navegador):

npx playwright test --headed


Abrir a interface interativa do Playwright (modo UI):

npx playwright test --ui

6. Declaração de Uso de IA

Conforme as diretrizes da disciplina, registro que o desenvolvimento deste teste, bem como a estruturação do README, foram realizados com apoio da IA ChatGPT (OpenAI), utilizada para auxílio técnico e revisão textual.