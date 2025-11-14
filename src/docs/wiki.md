# Plano e Execução de Testes – OrangeHRM

## Objetivo

Este documento descreve o **plano de testes** e a **execução dos testes automatizados** realizados na aplicação **OrangeHRM**, utilizando **Python e Selenium WebDriver**.  
O foco principal foi a validação da funcionalidade **“My Leave”**, que exibe e filtra solicitações de férias com base em intervalos de datas.

---

## PLANO DE TESTES

### Escopo

O plano de testes abrange a automação de cenários de interface gráfica (GUI) no módulo **Leave** do sistema OrangeHRM.  
Os testes garantem que as funcionalidades principais estejam acessíveis e exibam os resultados esperados após o login.

### Objetivo dos testes

Verificar:

- A correta exibição e filtragem de solicitações de licença no menu **“My Leave”**;
- O carregamento adequado da página **Leave**;
- A integridade visual e funcional dos elementos da interface.

### Ferramentas Utilizadas

- **Linguagem:** Python 3
- **Framework:** Selenium WebDriver
- **Navegador:** Google Chrome
- **Driver:** ChromeDriver
- **Ambiente de Execução:** VsCode
- **Assistência de IA:** ChatGPT (auxílio em downloads, comandos, configuração do ambiente e ajustes de execução)

---

## Cenários de Teste

### Cenário 1 – Verificar intervalo de datas em “My Leave” (Teste Principal - Corrigido)

1. Realizar login no sistema.
2. Acessar o menu “Leave” → “My Leave”.
3. Inserir um intervalo de datas (incluindo o cenário de datas invertidas para validação).
4. Aplicar o filtro e validar o resultado exibido, verificando a presença de resultados, a mensagem de "Nenhum Registro Encontrado" ou a mensagem de erro de validação de datas.

**Resultado esperado:**  
A página deve carregar corretamente e exibir as licenças correspondentes ao período selecionado, ou exibir a mensagem de erro de validação de datas, se aplicável.

### Cenário 2 – Recarregar página “Leave” (Teste Complementar)

1. Realizar login no sistema.
2. Acessar o menu “Leave”.
3. Recarregar a página.
4. Validar se os elementos principais permanecem acessíveis.

**Resultado esperado:**  
A página deve ser recarregada com sucesso, mantendo sua estrutura funcional e visual.

---

## EXECUÇÃO DOS TESTES

### Execução local

Os testes foram executados **localmente via terminal**, após configuração completa do ambiente Python e instalação das dependências.

Comandos utilizados:

```bash
pip install selenium
python my_leave_calendar_test.py
python test_leave_page_reload.py
```
