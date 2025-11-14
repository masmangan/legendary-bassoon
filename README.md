# Testes Automatizados – Login/Logout (OrangeHRM)

Este projeto contém um teste automatizado em **Python** utilizando **Selenium WebDriver** para validar a jornada completa de **Login e Logout** no sistema OrangeHRM Demo.

O objetivo é garantir que o fluxo de autenticação esteja funcionando corretamente, validando automaticamente cada etapa através de asserts.

------------------------------------------------------------

##  Funcionalidades testadas

- ✔️ Login com credenciais válidas
- ✔️ Login inválido (com assert)
- ✔️ Redirecionamento para o Dashboard
- ✔️ Abertura do menu do usuário
- ✔️ Logout
- ✔️ Retorno à página de Login

------------------------------------------------------------

##  Como executar o teste

1. Instale as dependências:
pip install selenium

2. Execute o script:
python tests/login_logout_test.py

O navegador abrirá automaticamente e realizará toda a jornada de forma visual.

------------------------------------------------------------

##  Estrutura do projeto

/tests
 └── login_logout_test.py
 └──README.md
 └──.gitignore
LICENSE

------------------------------------------------------------

##  Tecnologias utilizadas

- Python 3
- Selenium WebDriver
- Google Chrome / ChromeDriver
- OrangeHRM Demo

------------------------------------------------------------

##  Autor

Lucas Andrade
