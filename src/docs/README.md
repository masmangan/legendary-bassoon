# Teste de Intervalo de Datas no MyLeave (OrangeHRM)

## Explicação do Teste

Este documento descreve os testes automatizados desenvolvidos para validar a funcionalidade de **intervalo de datas** no módulo **MyLeave** do sistema **OrangeHRM**.  
O objetivo principal foi garantir que o sistema exiba corretamente os registros de solicitações de licença **dentro do intervalo de datas selecionado** pelo usuário.

---

## Fluxo Principal (Teste de Intervalo de Datas)

1. Realizar **login** no sistema com credenciais válidas.
2. Acessar o módulo **“My Leave”** no menu principal.
3. Preencher os campos de **data inicial** e **data final**.
4. Clicar em **“Search”** para aplicar o filtro.
5. Verificar se os resultados exibidos estão dentro do intervalo especificado ou se a mensagem de validação/erro apropriada é exibida.

**Resultado esperado:** O sistema deve exibir apenas as solicitações de licença que se encaixam no intervalo de datas selecionado.

---

## O que foi implementado

### Teste principal: `my_leave_calendar_test.py`

Automatiza o fluxo completo de validação do intervalo de datas no MyLeave, garantindo que o comportamento do sistema seja o esperado e incluindo asserções explícitas sobre a resposta da aplicação (resultados ou mensagens de validação).  
Esse foi o **foco principal do trabalho**.

### Teste complementar: `test_leave_page_reload.py`

Complementa o trabalho validando o **carregamento correto da página de Leave** após um reload.

---

## Tecnologias Utilizadas

| Categoria          | Ferramenta                  |
| ------------------ | --------------------------- |
| Linguagem          | Python                      |
| Biblioteca         | Selenium WebDriver          |
| Driver             | ChromeDriver                |
| Framework de Teste | unittest (nativo do Python) |

O **Selenium** foi usado para automatizar as interações com o navegador, simulando as ações reais do usuário no sistema.  
Além disso, foi utilizada **IA** para **auxílio em relação a comandos e configurações de download**.

---

## Preparação do Ambiente (Setup)

Antes de executar os testes, é necessário preparar o ambiente:

### Pré-requisitos

- Python 3 instalado
- Selenium instalado
- ChromeDriver compatível com a versão do Google Chrome

### Instalação do Selenium

```bash
pip install selenium
```
