# Trabalho T2: Teste do Orange Human Resource Management

Este repositório contém o trabalho T2 para a disciplina de Verificação e Validação de Software (2025/2), focado na implementação de um teste de sistema automatizado para a plataforma Orange HRM.

**Aluno:** Enzo Tonatto

---

## 1. Introdução

O sistema sob teste é o **Orange Human Resource Management (Orange HRM)**, uma conhecida plataforma de código aberto para gerenciamento de recursos humanos, frequentemente utilizada em cursos de teste de software.

O objetivo deste trabalho é aplicar técnicas de teste de sistema para validar uma "jornada de usuário" específica dentro da plataforma.

### 1.1. Informações do Projeto

* **Sistema:** Orange Human Resource Management (Orange HRM)
* **Código-fonte (Original):** `https://github.com/orangehrm/orangehrm`
* **Servidor de Testes:** `https://opensource-demo.orangehrmlive.com/`

### 1.2. Tecnologias Utilizadas

Os testes foram desenvolvidos utilizando a seguinte stack:

* **Linguagem:** Java
* **Framework de Teste:** JUnit 5 (Jupiter)
* **Automação de UI:** Selenium WebDriver
* **Gerenciamento de Dependências:** Apache Maven
* **Gerenciamento de Drivers:** WebDriverManager

### 1.3. Como Compilar e Rodar os Testes

Para executar o teste automatizado, siga os passos abaixo:

**Pré-requisitos:**

* Java JDK 11 ou superior
* Apache Maven
* Google Chrome (o teste está configurado para o `ChromeDriver`)

**Execução:**

1.  Clone este repositório.
2.  Abra um terminal na pasta raiz do projeto (onde o arquivo `pom.xml` está localizado).
3.  Execute o seguinte comando Maven:

    ```sh
    mvn test
    ```

O Maven irá baixar todas as dependências (incluindo Selenium e WebDriverManager), compilar o código e executar o teste JUnit. O resultado (`BUILD SUCCESS`) será exibido no terminal.

---

## 2. Objetivos

O objetivo principal deste projeto é implementar um teste de sistema automatizado para validar uma jornada de usuário crítica, aplicando as técnicas de teste discutidas em aula.

### 2.1. Jornada de Usuário Selecionada

A jornada de usuário escolhida foi a **"Edição de Informações Pessoais (Personal Details)"**, focando especificamente na alteração do campo "Estado Civil" (Marital Status).

> **História de Usuário:** "Como um usuário logado no sistema, eu quero navegar até a minha página de 'My Info', modificar meu 'Estado Civil', salvar essa alteração e ter a confirmação visual de que o dado foi persistido corretamente."

---

## 3. Casos de Teste

Com base na jornada de usuário, foi planejado e implementado o seguinte caso de teste de sistema:

| ID | Descrição | Pré-condições | Passos | Resultado Esperado | Status |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **CT-001** | **Caminho Feliz:** Editar "Estado Civil" com sucesso. | Usuário "Admin" logado. | 1. Navegar para "My Info".<br>2. Ler o "Marital Status" atual.<br>3. Selecionar um valor *diferente* (ex: se "Single", selecionar "Married"; se não for "Single", selecionar "Single").<br>4. Rolar a tela para expor o botão "Salvar".<br>5. Clicar em "Salvar".<br>6. Esperar o pop-up de sucesso.<br>7. Recarregar a página.<br>8. Verificar se o novo valor foi salvo. | O pop-up de sucesso é exibido e o novo valor é persistido após o recarregamento. | **PASSOU** |

---

## 4. Resultado dos Testes

O caso de teste **CT-001** (`testEditMaritalStatus`) foi implementado com sucesso. Após um processo de depuração significativo (detalhado na "Jornada de Construção"), o teste agora é executado de forma estável e passa consistentemente.

* `testEditMaritalStatus()`: **PASSOU**

Um **defeito** (ou comportamento inesperado) do sistema foi identificado durante os testes: a plataforma exibe um pop-up de "Sucesso" mesmo quando o backend falha em validar e salvar a alteração (como observado ao tentar mudar do valor padrão `"<-- Select -->"` para `"Single"`).

Para contornar isso, a asserção final do teste foi robustecida: ela não confia no pop-up de sucesso, mas sim **recarrega a página (`driver.navigate().refresh()`)** e verifica se o dado foi **realmente persistido** no banco de dados.

---

## 5. Jornada de Construção (Diário de Bordo)

Esta seção relata a evolução do trabalho ao longo de três dias, destacando os desafios e as decisões de projeto que levaram ao teste final.

### 🗓️ Dia 1: Configuração e A Luta contra o SafariDriver

**Decisões de Stack:**
O projeto foi configurado com Java e Maven pela facilidade no gerenciamento de dependências. A escolha pelo **Selenium WebDriver** foi natural, pois é a ferramenta padrão de mercado para testes de sistema *end-to-end*, permitindo a automação direta do navegador.

**O Problema (Safari):**
Minha primeira tentativa foi usar o `SafariDriver` por ser nativo do macOS. Esta decisão provou ser um erro custoso. Gastei várias horas depurando por que o script falhava. O `SafariDriver` mostrou-se extremamente instável, incapaz de interagir corretamente com os formulários do Orange HRM. Tentativas de clique (`.click()`) e submissão (`.submit()`) falhavam silenciosamente, tornando impossível o desenvolvimento do teste.

**Solução:** Abandonei o Safari e reverti para a stack padrão de mercado: **`ChromeDriver`** e **`WebDriverManager`**. Imediatamente, o script conseguiu ao menos logar e navegar, provando que o problema era o driver, e não o script.

### 🗓️ Dia 2: O Formulário Instável e a Primeira Tentativa (Nome)

**O Desafio (Campos de Texto):**
Com o `ChromeDriver` funcionando, meu primeiro objetivo foi implementar um teste para alterar o nome do usuário (`testEditName`). Aqui, encontrei o segundo grande obstáculo: formulários dinâmicos (provavelmente em React/Vue).

* **Falha 1 - Limpar o Campo:** O script era rápido demais. Tentar limpar o campo com `Keys.CONTROL + "a"` ou `.clear()` falhava de forma inconsistente. O site não "via" a mudança de valor, e o botão "Salvar" permanecia desabilitado. Isso levou a um `TimeoutException` (o script esperava o botão ficar clicável, o que nunca acontecia).

* **Falha 2 - `ElementClickInterceptedException`:** Nos raros casos em que o botão *era* habilitado, o `.click()` falhava. O log do Selenium indicou que a barra de menu superior (`oxd-topbar-header-userarea`) estava fisicamente **cobrindo** o botão "Salvar", interceptando o clique.

**Solução (Pivô):** O teste de alteração de nome se mostrou muito instável ("flaky"). Decidi pivotar para um componente de UI mais simples e com menos "estado": o dropdown **"Marital Status"**.

### 🗓️ Dia 3: A "Fórmula Vencedora" e o Sucesso

**O Desafio (O Clique Final):**
O `testEditMaritalStatus` foi mais fácil. Mudar o dropdown disparou o evento de "mudança" e habilitou o botão "Salvar" de forma confiável. No entanto, o erro de **`ElementClickInterceptedException`** (o botão coberto pela barra de menu) persistiu.

**Tentativas e Falhas:**
Tentei usar `JavascriptExecutor.click()` para "forçar" o clique. Isso evitou o erro de interceptação, mas criou um **falso positivo**:

* O `JavascriptExecutor` "clicou" no botão.
* O frontend mostrou o pop-up de "Sucesso" (o `wait.until` passou!).
* Porém, o clique falso **não enviou os dados ao servidor**.
* O teste falhou na asserção final, pois o valor antigo (`<-- Select -->`) ainda estava lá após o recarregamento (`expected: <Single> but was: <-- Select -->`).

**A "Fórmula Vencedora" (A Solução):**
A solução final exigiu uma combinação de todas as lições aprendidas:

1.  **Resolver Interceptação:** Usei `JavascriptExecutor` não para clicar, mas para **rolar a tela** (`.scrollIntoView(false)`), movendo o botão para a parte inferior da tela, longe da barra de menu.
2.  **Resolver Timing:** Adicionei pequenas pausas (`Thread.sleep(500)`) após cliques e recarregamentos. Isso deu ao framework JS do site o tempo necessário para "respirar" e processar as mudanças, como apontado nos testes.
3.  **Usar um Clique Real:** Com o botão agora visível e não interceptado, um `.click()` **real** foi usado.

**Resultado:** O clique real enviou os dados ao servidor. O pop-up de sucesso apareceu *e* os dados foram persistidos. O teste `testEditMaritalStatus` passou de forma estável e confiável.

## 6. Uso de Ferramentas de IA

Conforme exigido pelo enunciado do trabalho, esta seção registra o uso de ferramentas de IA no desenvolvimento deste projeto.

Utilizei o assistente de IA **Gemini (Google)** para as seguintes finalidades:

* **Depuração de Erros (Debugging):** O Gemini foi fundamental para diagnosticar e corrigir uma série de erros complexos do Selenium WebDriver. Isso incluiu a análise de *stack traces* para identificar a causa raiz de exceções como:
    * `TimeoutException` (indicando que o script era rápido demais para o site).
    * `ElementClickInterceptedException` (identificando que a barra de menu cobria o botão "Salvar").
    * Falhas de `AssertionFailedError` (ajudando a depurar por que os dados não estavam sendo persistidos corretamente).
* **Construção do Relatório:** O Gemini auxiliou na estruturação, geração de texto e formatação deste `README.md`, ajudando a organizar a "Jornada de Construção" e a articular os desafios técnicos encontrados.