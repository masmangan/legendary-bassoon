# Setup em até 5 passos (Windows)

Opção A — venv já versionado (3 passos):
1) Ativar venv:
```bash
.\orange_tests\venv\Scripts\Activate.ps1
```
2) Rodar testes:
```bash
orange_tests\venv\Scripts\python.exe -m pytest -c orange_tests\pytest.ini orange_tests\tests
```
3) Gerar relatório HTML:
```bash
orange_tests\venv\Scripts\python.exe -m pytest -c orange_tests\pytest.ini --html=orange_tests\reports\html\report.html --self-contained-html orange_tests\tests
```

Opção B — sem venv no repositório (5 passos):
1) Criar venv:
```bash
python -m venv orange_tests\venv
```
2) Ativar venv:
```bash
.\orange_tests\venv\Scripts\Activate.ps1
```
3) Instalar dependências:
```bash
pip install -r orange_tests\requirements.txt
```
4) Rodar testes:
```bash
python -m pytest -c orange_tests\pytest.ini orange_tests\tests
```
5) Gerar relatório HTML:
```bash
python -m pytest -c orange_tests\pytest.ini --html=orange_tests\reports\html\report.html --self-contained-html orange_tests\tests
```

Relatórios (gerados automaticamente):
- HTML: `orange_tests\reports\html\report.html`
- JUnit: `orange_tests\reports\xml\junit.xml`
- Logs: `orange_tests\reports\logs\pytest.log`
- Screenshots: `orange_tests\reports\screenshots\*.png` (para testes “passed” e “failed”)

## Tipos de Testes

- Testes de interface (E2E) com Selenium WebDriver (Firefox).
- Jornada de usuário positiva: atualização de “Organization Name” e “Phone”.
- Jornada de usuário negativa: validação de campo obrigatório (mensagem “Required”).

## Técnicas Utilizadas

- Asserções de persistência de valores e mensagens de validação.
- Geração de relatórios (HTML, JUnit XML, logs) e screenshots automáticas.

## Relatórios e Artefatos

- HTML: `orange_tests\reports\html\report.html`
- JUnit XML: `orange_tests\reports\xml\junit.xml`
- Logs: `orange_tests\reports\logs\pytest.log`
- Screenshots: `orange_tests\reports\screenshots\*.png`

- Com venv versionado:
```bash
.\orange_tests\venv\Scripts\Activate.ps1
```
- Rodar testes:
```bash
orange_tests\venv\Scripts\python.exe -m pytest -c orange_tests\pytest.ini orange_tests\tests
```
// ... existing code ...