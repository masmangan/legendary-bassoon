# Teste E2E – Esqueci Minha Senha (Forgot Password) | OrangeHRM | Matheus de Oliveira Ferreira

## Descrição

Este teste automatizado valida o fluxo de recuperação de senha no sistema **[OrangeHRM Demo](https://opensource-demo.orangehrmlive.com/)**.  
O objetivo é verificar se, ao solicitar o reset de senha, o sistema exibe a mensagem de sucesso confirmando o envio do link de redefinição.

O teste é **E2E (End-to-End)**, desenvolvido com **Python + Selenium + Pytest**, e usa o `webdriver-manager` para gerenciar automaticamente o driver do Chrome (sem precisar de `chromedriver.exe` manual).

---

## Estrutura do Projeto

forgotPassword/
│
├── test_forgot_password.py # Script principal do teste
├── print.png # Screenshot final do teste (gerado automaticamente no final do teste)
└── README.md # Arquivo de explicação


---

## Lógica do teste

1. Abre a página de login do OrangeHRM Demo.  
2. Clica no link **“Forgot your password?”**.  
3. Preenche o campo com o usuário **Admin**.  
4. Clica em **Reset Password**.  
5. Valida uma das seguintes condições:
   - Aparece um com a mensagem:  
     `Reset Password link sent successfully`
   - Ou redireciona para a tela de confirmação (`sendPasswordReset`).

Se uma dessas condições for verdadeira, o teste passa.

---

## Requisitos

- Python 3.10+  
- Google Chrome instalado  
- Internet ativa (neste caso baixa o driver automaticamente para abrir o chrome)

Bibliotecas necessárias:
```bash
pip install selenium webdriver-manager pytest pytest-html

---
