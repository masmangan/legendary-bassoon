# Teste de Sistema: Edição de "My Info"

## 1\. Contexto do Projeto

Este teste faz parte das entregas do **Trabalho T2** da disciplina de Verificação e Validação de Software (PUCRS, 2025/II).

  * **Sistema Alvo:** Orange Human Resource Management (Servidor de Demo)
  * **Repositório:** `https://github.com/masmangan/legendary-bassoon`
  * **Branch:** `edit-personal-details`
  * **Autor:** Pedro Augusto Pereira

-----

## 2\. Objetivo do Teste

O objetivo deste script é executar um **Teste de Sistema** focado na jornada do usuário ao editar suas próprias informações pessoais através da tela "My Info".

O teste valida o fluxo completo da interação do usuário com o formulário, desde o login até a confirmação da ação de salvamento.

### Jornada de Usuário Testada

A jornada de usuário validada por este script é:

1.  O usuário faz login com credenciais de "Admin".
2.  O usuário navega até a tela "My Info" no menu lateral.
3.  O usuário preenche os campos editáveis do formulário (Nome, Sobrenome, CNH, Data de Licença, etc.).
4.  O usuário clica no botão "Save" para submeter as alterações.
5.  O sistema apresenta ao usuário uma notificação visual de sucesso ("Successfully Updated").

-----

## 3\. Tecnologia Utilizada

O teste foi **implementado** usando **Playwright**, uma biblioteca moderna de automação de testes E2E para Node.js, que permite a criação de scripts robustos para interagir com navegadores web.

-----

## 4\. Como Instalar e Rodar o Teste

### 4.1. Pré-requisitos

  * Node.js (versão 16 ou superior)
  * npm (gerenciador de pacotes do Node)

### 4.2. Instalação das Dependências

1.  Clone o repositório.
2.  Mude para a branch correta:
    ```bash
    git checkout edit-personal-details
    ```
3.  Abra o terminal na pasta do projeto.
4.  Instale o Playwright:
    ```bash
    npm install @playwright/test
    ```
5.  Instale os navegadores que o Playwright utiliza:
    ```bash
    npx playwright install
    ```

### 4.3. Execução do Teste

Para rodar todos os testes de forma "headless" (em segundo plano):

```bash
npx playwright test
```

Para rodar os testes abrindo o navegador (modo "headed"):

```bash
npx playwright test --headed
```

Para abrir a interface de usuário do Playwright (recomendado para depuração):

```bash
npx playwright test --ui
```

-----

## 5\. Declaração de Uso de IA

Conforme exigido pelo plano de ensino, registro que a **redação deste relatório** e o **entendimento sobre o funcionamento da biblioteca Playwright (Node.js)** foram realizados com o auxílio da IA Gemini (Google).