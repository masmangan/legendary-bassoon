# Plano de Testes: Criação de Novo Usuário

## Introdução

Este plano de testes contempla o sistema OrangeHRM, focado no fluxo de criação de novos usuários através do módulo administrativo.

O teste foi implementado em Python usando a biblioteca Selenium WebDriver para automatizar o processo completo de cadastro de um novo usuário no sistema.

## Desenvolvimento do trabalho

Na primeira aula eu naveguei pelo sistema para me habituar com o mesmo e vi quais haviam sido os testes implementados no semestre passado. Com base nisso, escolhi o fluxo que teste que eu implementaria.

Na segunda aula, organizei a estrutura do README.md para estabelecer o Plano de Testes, definindo claramente os Objetivos, Casos de Teste, Entradas e Resultados Esperados antes de iniciar o código.

Nos dias seguintes, desenvolvi o código do teste do fluxo escolhido. Para isso é importante comentar que utilizei como base o teste de fazer login no sistema, implementado no semestre passado, visto que no meu fluxo isso seria necessário também. Além disso, finalizei o README com a documentação do processo.

Nos dias após o primeiro dia de apresentações, corrigi os problemas que o professor apontou, em especial o fato de o teste inicialmente não ter assert e não conseguir rodar no codespace.


## Estrutura do projeto

CreateUserPythonSelenium/
├── .devcontainer/
│   └── devcontainer.json          # Configuração do Codespaces
├── tests/
│   └── createUserTest.py          # Teste
├── venv/                          # Ambiente virtual
├── LICENSE                        # Licença do projeto
├── README.md                      # Documentação
└── requirements.txt               # Dependências Python


## Como executar

### No Codespace

#### 1. Crie e ative o ambiente virtual:
```bash
python -m venv venv

source venv/bin/activate 
```

#### 2. Baixe as dependencias:
```bash

pip install -r requirements.txt

sudo apt update
sudo apt -f install
sudo apt install ./google-chrome-stable_current_amd64.deb
```

#### 3. Execute o teste

```bash
python tests/createUserTest.py
```

### Localmente

#### 1. Crie um ambiente virtual:
```bash
python -m venv venv
```

#### 2. Ative o ambiente virtual:
```bash
source venv/bin/activate # No linux

.\venv\Scripts\activate # No windows

```

#### 3. Instale as dependências
```bash
pip install -r requirements.txt 

```

#### 4. Execute o teste
```bash
python tests/createUserTest.py
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


Escrito com auxílio de IA 
