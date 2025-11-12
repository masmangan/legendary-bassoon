# 🔍 Projeto de Testes Automatizados - OrangeHRM (Python/pytest)

## 📋 Descrição

Projeto de testes automatizados **convertido para Python/pytest** focado **exclusivamente na funcionalidade de pesquisa de funcionários** no sistema OrangeHRM.

### ✅ Otimizações Realizadas

- **Conversão para Python/pytest**: Maior estabilidade e simplicidade de execução.
- **Execução Fluida**: O navegador abre e fecha **apenas uma vez** (`@pytest.fixture(scope="session")`).
- **Sincronização Otimizada**: Uso de **Explicit Waits (WebDriverWait)** de 20 segundos para máxima estabilidade.
- **Validação Robusta**: Uso de nome de funcionário estável ("Paul Collings") e validação simplificada para garantir o sucesso do teste.
- **Navegador Visível**: O Chrome é aberto em modo visível.

---

## 🚀 Como Executar

### Pré-requisitos
1.  **Python 3.10+** instalado.
2.  **Google Chrome** instalado.

### 1. Instalar Dependências
```bash
# Crie e ative um ambiente virtual (recomendado)
python3 -m venv venv
source venv/bin/activate  # No Windows: .\venv\Scripts\activate

# Instale as dependências
pip install selenium pytest webdriver-manager
```

### 2. Executar o Teste
```bash
# Certifique-se de estar no diretório 'orangehrm_python'
pytest tests/test_search_employee.py
```

---

## 🎯 Cenário de Teste Implementado

### Teste de Busca Completo (Otimizado)
- **Pré-requisito**: Login (executado apenas uma vez)
- Navega para PIM → Employee List
- Busca funcionário existente (**Paul Collings**)
- Valida se há resultados na tabela
- Busca funcionário inexistente (**Nome Inexistente 123**)
- Valida mensagem "No Records Found"

---

## 🌐 Navegador Visível e Otimizado

- ✅ Modo headless **DESABILITADO**
- ✅ Janela do Chrome será maximizada
- ✅ **Abre e fecha apenas uma vez**
- ✅ Execução mais rápida e visualmente mais fluida

---

## 📁 Estrutura do Projeto

```
orangehrm_python/
├── pages/
│   ├── BasePage.py
│   ├── LoginPage.py
│   └── PIMPage.py
├── tests/
│   └── test_search_employee.py
├── README.md
└── venv/ (ambiente virtual)
```

---

**Status**: ✅ **CONVERTIDO PARA PYTHON - MÁXIMA ESTABILIDADE**
