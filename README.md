# 🧪 Testes Automatizados – OrangeHRM

Este projeto contém testes funcionais e de validação realizados na aplicação **OrangeHRM (versão demo)**:

https://opensource-demo.orangehrmlive.com/

Os testes foram desenvolvidos utilizando **Python + Selenium + Pytest**.

---

## 🎯 Objetivo

Validar a funcionalidade de **gerenciamento de cargos (Job Titles)** na interface administrativa do sistema, garantindo:

- Criação correta de novos cargos
- Validação de entradas inválidas

---

## 🛠 Tecnologias Utilizadas

| Ferramenta | Uso |
|-----------|-----|
| Python 3.x | Linguagem |
| Selenium WebDriver | Automação Web |
| Pytest | Estrutura de testes |
| webdriver-manager | Gerenciamento automático do ChromeDriver |
| Google Chrome | Navegador |

---

## ✅ Casos de Teste Documentados

### **CT01 – Criar Cargo com Sucesso**
**Descrição:** Verificar se o sistema permite cadastrar um cargo válido.

**Resultado:** ✅ Aprovado  
O cargo foi criado e exibido corretamente na lista.

**Trecho do teste:**
```python
def test_create_job_title(driver):
    login = LoginPage(driver)
    login.login("Admin", "admin123")

    job_page = JobTitlesPage(driver)
    job_page.open_job_titles()
    job_page.create_job_title("QA Automation Tester")
    job_page.search_job_title("QA Automation Tester")

    assert job_page.job_title_exists("QA Automation Tester") is True
```

---

### **CT02 – Validação de Campo**
**Descrição:** Verificar se entradas vazias ou inválidas são rejeitadas.

**Resultado:** ✅ Aprovado  
Strings vazias e com espaços foram corretamente identificadas como inválidas.

**Trecho do teste:**
```python
def test_validate_job_title():
    assert validate_job_title("QA Engineer") == True
    assert validate_job_title("") == False
    assert validate_job_title("   ") == False
```

---

## 📊 Resultado da Execução

```
==============================================
2 passed in 21.87s
==============================================
```

| Caso | Status |
|------|--------|
| CT01 – Criar cargo válido | ✅ Aprovado |
| CT02 – Validação de campos | ✅ Aprovado |

---

## 🧾 Conclusão

A funcionalidade de gerenciamento de cargos se mostrou estável e consistente.  
O sistema validou corretamente tanto:
- a criação de cargos válidos, quanto
- a rejeição de entradas inválidas.
