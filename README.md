# Teste Automatizado do Formulário "Contact Sales" - Orange HRM

Este projeto contém um script em Python que automatiza o teste do formulário "Contact Sales" do site [Orange HRM](https://www.orangehrm.com/en/contact-sales). O objetivo é validar a funcionalidade de verificação de dados inválidos, como nome, email e telefone, e garantir que o sistema exiba mensagens de erro apropriadas.

## Pré-requisitos

Antes de executar o teste, certifique-se de ter instalado e configurado os seguintes itens:

### 1. Python

- Instale o Python 3.x:
    [https://www.python.org/downloads]

- Verifique a instalação:
    No terminal digite: python --version

## 2. Selenium

Instale a biblioteca Selenium para Python com:
    pip install selenium

## 3. Google Chrome

Instale o navegador Google Chrome se necessário (versão compatível com o ChromeDriver):

[https://www.google.com/chrome]

## 4. ChromeDriver

* Baixe o ChromeDriver compatível com sua versão do Chrome:
    [https://sites.google.com/chromium.org/driver]

* Extraia o arquivo `chromedriver.exe` (Windows) ou `chromedriver` (Linux/Mac).

* Coloque o executável em uma pasta acessível, preferencialmente na mesma pasta do script Python ou em uma pasta incluída no PATH do sistema.

* Para testar se o ChromeDriver está acessível, abra o terminal e digite:

```bash
chromedriver
```

Deve abrir uma janela indicando que o ChromeDriver está rodando.

## Como executar o teste

1. Clone ou baixe este repositório.

2. Navegue até a pasta do projeto no terminal.

3. Execute o script Python com:
    python test_contact_sales_form.py

## Fluxo do teste

1. O navegador Chrome será aberto automaticamente e o formulário será preenchido com dados inválidos.

2. Quando o script pedir, complete manualmente o reCAPTCHA na janela do navegador.

3. O script tentará enviar o formulário e exibirá no terminal as mensagens de erro detectadas.

4. Após a execução, o navegador será fechado automaticamente.

## Observações

* O reCAPTCHA não pode ser automatizado por bots, por isso a pausa para completar manualmente.

* Certifique-se de usar a versão correta do ChromeDriver compatível com seu navegador.

## Referências

* Selenium WebDriver para Python:
    [https://selenium-python.readthedocs.io]

* ChromeDriver:
    [https://sites.google.com/chromium.org/driver]

* Google Chrome:
    [https://www.google.com/chrome]