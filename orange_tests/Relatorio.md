# Relatório de Testes de Sistema — OrangeHRM (Demo) — Organização

Nota de autoria: Este relatório e os testes foram gerados com auxílio de IA.

## Introdução

- Sistema testado: Módulo “Admin > General Information” do OrangeHRM Demo (`https://opensource-demo.orangehrmlive.com`), usando usuário `Admin` e senha `admin123`.
- Abordagem de teste:
  - Automação com Selenium WebDriver (Firefox) e Pytest.
  - Fixtures no `conftest.py` realizam o login, navegam para a página de “General Information” e fazem logout ao final.
  - Sincronização com `WebDriverWait` (10s) e espera implícita (5s); habilitação de edição via seletor `.oxd-switch-input`; salvamento com `button[type='submit']`.
- Onde obter o código-fonte:
  - Código local do projeto: `legendary-bassoon-lucas-silva\orange_tests\`.
  - Estrutura relevante:
    - `orange_tests\tests\test_organization_update.py`
    - `orange_tests\tests\test_organization_required_field.py`
    - `orange_tests\tests\conftest.py`
    - `orange_tests\requirements.txt`
    - `orange_tests\pytest.ini`
- Como compilar e rodar os testes:
  - Compilação: não há etapa de compilação (projeto Python).
  - Pré-requisitos:
    - Python 3.x e `pip` instalados no Windows.
    - Internet ativa (o site Demo é acessado online).
    - Navegador Firefox instalado; o Selenium Manager normalmente cuida do `geckodriver`. Se necessário, instale o `geckodriver` e adicione ao `PATH`.
  - Instalação e execução:
    - Criar ambiente virtual:
      ```bash
      python -m venv orange_tests\venv
      ```
    - Ativar o ambiente:
      ```bash
      orange_tests\venv\Scripts\activate
      ```
    - Instalar dependências:
      ```bash
      pip install -r orange_tests\requirements.txt
      ```
    - Rodar os testes (opção 1 — dentro da pasta):
      ```bash
      cd orange_tests
      ```
      ```bash
      pytest
      ```
    - Rodar os testes (opção 2 — da raiz usando o `pytest.ini`):
      ```bash
      pytest -c orange_tests\pytest.ini orange_tests\tests
      ```
  - Configuração de saída:
    - `orange_tests\pytest.ini` define `addopts = -v -s` para saída verbosa e logs em tempo real.

## Objetivo

- Objetivo geral: validar duas “jornadas de usuário” típicas no módulo de Organização do OrangeHRM, segundo práticas de Engenharia de Software:
  - Jornada 1: “Administrador atualiza as informações gerais da organização”.
    - Persona: Administrador autenticado.
    - Pré-condição: Login válido; acesso à página “General Information”.
    - Passos chave: habilitar edição, alterar `Organization Name` e `Phone`, salvar e confirmar persistência.
    - Resultado esperado: valores atualizados persistem e são exibidos corretamente após salvar.
  - Jornada 2: “Administrador tenta salvar sem preencher um campo obrigatório”.
    - Persona: Administrador autenticado.
    - Pré-condição: Login válido; acesso à página “General Information”.
    - Passos chave: habilitar edição, limpar `Organization Name`, salvar.
    - Resultado esperado: exibição de mensagem de validação “Required” para o campo obrigatório.

## Casos de teste

- CT-01 — Atualização de informações gerais (arquivo `test_organization_update.py`)
  - Contexto:
    - Login realizado por `logged_in_driver` (fixture com escopo `module`).
    - Navegação automática para `Admin > Organization > General Information`.
  - Dados de entrada:
    - `Organization Name`: valor novo dinâmico (`Org Teste {timestamp[-5:]}`).
    - `Phone`: valor novo dinâmico (`timestamp[-9:]`).
  - Passos principais:
    - Habilitar edição (.oxd-switch-input).
    - Substituir `Organization Name` e `Phone`.
    - Salvar (`button[type='submit']`).
    - Esperar que os campos mostrem os novos valores via `EC.text_to_be_present_in_element_value`.
  - Verificações:
    - `assert org_name_display == new_org_name`
    - `assert phone_display == new_phone`
- CT-02 — Validação de campo obrigatório (arquivo `test_organization_required_field.py`)
  - Contexto:
    - Login realizado por `logged_in_driver`.
  - Dados de entrada:
    - `Organization Name`: vazio (após limpar com `CTRL+A` e `DELETE`).
  - Passos principais:
    - Habilitar edição (.oxd-switch-input).
    - Limpar o campo `Organization Name`.
    - Salvar (`button[type='submit']`).
    - Localizar a mensagem de erro pelo seletor
      `//label[text()='Organization Name']/ancestor::div[contains(@class,'oxd-input-group')]//span[contains(@class,'oxd-input-field-error-message')]`.
  - Verificações:
    - `assert "Required" in error_message_element.text`

## Resultado dos testes

- Ambiente de execução:
  - Testes exigem internet ativa e acesso ao site Demo do OrangeHRM.
  - Firefox deve estar operacional; em ambientes sem `geckodriver`, o Selenium Manager tenta providenciar automaticamente.
- Status esperado:
  - Com os pré-requisitos atendidos, ambos os testes devem passar, pois:
    - Asserções verificam a presença do texto “Required” para campo obrigatório.
    - As alterações de `Organization Name` e `Phone` são aplicadas e confirmadas por leituras de valor pós-salvamento.
- Defeitos identificados:
  - Não foram observados defeitos a partir da análise estática do código de teste.
  - Possíveis falhas na execução costumam estar relacionadas ao ambiente (rede indisponível, indisponibilidade do site Demo, falha de driver/navegador).

## Observações finais

- Fixtures:
  - `driver` (escopo `session`): inicializa Firefox com `implicitly_wait(5)` e `yield driver`.
  - `logged_in_driver` (escopo `module`): executa login (`Admin/admin123`), navega para `Admin_URL = .../admin/viewOrganizationGeneralInformation`, e realiza logout ao final (valida retorno à tela de login).
- Tecnologias:
  - Selenium, Pytest (`requirements.txt` lista `selenium` e `pytest`).

## Armazenamento de Resultados

- HTML: `reports\report.html` (relatório visual gerado com pytest-html).
- JUnit XML: `reportsjunit.xml` (compatível com CI/CD).
- Logs: `reportspytest.log` (logs de execução em nível `INFO`).
- Screenshots: `orange_tests\reports\screenshots\*.png` (capturadas para testes com status “passed” e “failed”).

### Observação
- Relatórios e testes gerados com apoio de IA.