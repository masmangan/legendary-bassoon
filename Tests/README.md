Testes Automatizados – Login/Logout (OrangeHRM)

Este repositório contém um teste automatizado desenvolvido em Python usando Selenium WebDriver para validar a jornada de usuário de Login e Logout no sistema OrangeHRM Demo.

O objetivo é garantir que o fluxo principal de autenticação funcione corretamente.

Como executar o teste
1. Instale as dependências
pip install selenium

2. Execute o script
python tests/login_logout_test.py


O navegador abrirá automaticamente e realizará:

Login com credenciais válidas

Verificação do Dashboard

Logout

Retorno à página de Login

 Funcionalidades testadas

Login válido

Login inválido (assert)

Acesso ao Dashboard

Logout e retorno à tela de Login

Asserts para validação automática

 Estrutura do projeto
/tests
   └── login_logout_test.py
   └── README.md
   └──.gitignore
LICENSE

 Ferramentas utilizadas

Python 3

Selenium WebDriver

Google Chrome / ChromeDriver

OrangeHRM Demo

 Autor

Lucas Andrade
