# Plano de Testes: Criação de Novo Usuário

## Introdução

Este plano de testes contempla o sistema OrangeHRM, focado no fluxo de criação de novos usuários através do módulo administrativo.

O teste foi implementado em Python usando a biblioteca Selenium WebDriver para automatizar o processo completo de cadastro de um novo usuário no sistema.

## Como executar

### 1. Crie um ambiente Virtual
```bash
python3 -m venv venv

source venv/bin/activate  # No Linux/macOS

.\venv\Scripts\activate  # No Windows
```

### 2. Instale as dependências

Certifique-se de estar na pasta do projeto:
```bash
pip install -r requirements.txt
# deve conter selenium e outras dependências necessárias
```

### 3. Execute o teste

Para criação de novo usuário:
```bash
python3 tests/createUserTest.py
```

## Objetivos

A jornada de usuário contempla:

### Criação de novo usuário no módulo Admin:

1. Entrar no site do OrangeHRM;
2. Se logar no site, com usuário e senha;
3. Navegar para a aba Admin no menu lateral;
4. Clicar no botão "Add" para abrir o formulário de criação;
5. Selecionar o User Role como "Admin";
6. Preencher o campo Employee Name selecionando um funcionário existente;
7. Selecionar o Status como "Enabled";
8. Preencher o campo Username com um nome único gerado aleatoriamente;
9. Preencher os campos de Password e Confirm Password;
10. Confirmar o envio dos dados, clicando no botão "Save";
11. Verificar a mensagem de sucesso após a criação.

## Casos de Teste

### Criar novo usuário administrativo:

**Cenário:** Cadastrar um novo usuário com permissões de administrador.

**Entradas:** 
- User Role: "Admin"
- Employee Name: Primeiro funcionário disponível (pesquisa com "a")
- Status: "Enabled"
- Username: Gerado aleatoriamente (formato: `testuser####`)
- Password: "Test@123"
- Confirm Password: "Test@123"

**Passos:** Login → Admin → Add → Selecionar Role → Selecionar Employee → Selecionar Status → Inserir Username → Inserir Passwords → Save

**Resultado Esperado:** Mensagem de sucesso exibida e usuário criado no sistema.

## Execução dos Testes

### Ambiente de teste:

- **Sistema:** Windows 11
- **Python:** 3.11.7
- **Navegador:** Google Chrome
- **Biblioteca de automação:** Selenium
- **Método de execução:** linha de comando via terminal PowerShell ou Bash

## Resultados dos testes

### Criar novo usuário administrativo:

**Resultado:** Passou ✅

**Observações:** 
1. Usuário criado com sucesso e mensagem de confirmação exibida. O username gerado aleatoriamente garante unicidade em cada execução do teste, evitando conflitos com usuários existentes.
2. Se o usuário gerado já existir o teste irá falhar
