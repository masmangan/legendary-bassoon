# Testes Selenium - Criar Vaga de Trabalho (Orange HRM)

**Aluno: Pedro Zardin Guimarães**
**Trabalho T2 - Verificação e Validação de Software**
**PUCRS - 2025/II**

---

## Sobre o Projeto

Testes automatizados E2E (end-to-end) com Selenium para a funcionalidade de **criação de vagas de trabalho** no sistema Orange HRM.

**Sistema testado:** [Orange HRM Demo](https://opensource-demo.orangehrmlive.com)

---

## Instalação

### Pré-requisitos
- Python 3.8+
- Google Chrome instalado
- Conexão com internet

### Setup

```bash
pip install -r requirements.txt

pytest -v
```

---

## Estrutura

```
CreateJobOffer/
├── tests/
│   ├── config.py              # Configurações
│   ├── conftest.py            # Fixtures pytest
│   ├── pages/                 # Page Objects
│   │   ├── base_page.py
│   │   ├── login_page.py
│   │   └── recruitment_page.py
│   └── test_system_create_job_vacancy.py
├── requirements.txt
├── pytest.ini
└── README.md
```

---

## Teste Implementado

### `test_create_vacancy_complete_flow`

**Fluxo completo:** Login → Navegação → Criação → Salvamento

**Passos do teste:**
1. Login no sistema com credenciais Admin
2. Navegar para módulo Recruitment > Vacancies
3. Clicar em Add para criar nova vaga
4. Preencher formulário passo a passo:
   - Vacancy Name
   - Job Title (dropdown)
   - Description
   - Hiring Manager (autocomplete)
   - Number of Positions
5. Clicar em Save

**Aguarda 5 segundos** ao final para visualização manual do resultado.

---

## Como Executar

```bash
pytest -v 
```

---

## Page Object Model

O projeto usa o padrão **Page Object Model** para separar lógica de teste da interação com UI.

**Page Objects criados:**
- `BasePage`: Métodos base reutilizáveis
- `LoginPage`: Página de login
- `RecruitmentPage`: Módulo de recrutamento e criação de vagas

---

## Tecnologias

- **Python 3.10**
- **Selenium 4.15.2**
- **Pytest 7.4.3**
- **WebDriver Manager 4.0.1**

---

## Jornada de Usuário Testada

**Título:** Criar Vaga de Trabalho

**Fluxo:**
1. Usuário faz login no sistema
2. Acessa módulo Recruitment
3. Clica em Vacancies
4. Clica em Add para criar nova vaga
5. Preenche formulário com dados da vaga
6. Clica em Save
7. Sistema valida e exibe mensagem de sucesso
8. Vaga aparece na listagem

---

## Observações

**Uso de IA:** Este projeto utilizou Claude Sonnet 4.5 (via Cursor) para estruturação do código e geração dos testes.