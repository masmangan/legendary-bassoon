# Relatório de Testes – OrangeHRM

## Descrição Geral

Este relatório documenta os **testes automatizados** realizados no sistema **OrangeHRM**, com foco no módulo **Leave**, desenvolvidos em **Python** utilizando o framework **Selenium WebDriver**.

O objetivo principal deste trabalho foi validar a **jornada de usuário** de filtragem de licenças no módulo “Leave” — especialmente a funcionalidade **My Leave**, que permite ao usuário visualizar e filtrar suas solicitações de férias/licenças em um intervalo de datas definido, conforme a técnica de teste de jornada de usuário (User Journey Testing).

Durante o desenvolvimento, foi utilizado **apoio de IA** para auxiliar na configuração do ambiente, instalação de dependências, download de ferramentas e execução de comandos de terminal.

---

## Testes Desenvolvidos

### Teste 1 – My Leave Calendar (Principal - Corrigido)

- **Arquivo:** `my_leave_calendar_test.py` (Versão Corrigida)
- **Objetivo:** Validar a funcionalidade de filtro de licenças, assegurando que o sistema exiba corretamente as solicitações dentro de um intervalo de datas e, crucialmente, testar a validação de datas invertidas, garantindo que a lógica de asserção do teste cubra tanto a exibição de resultados quanto a mensagem de "Nenhum Registro Encontrado" (No Records Found) ou a mensagem de erro de validação para períodos inválidos.
- **Etapas executadas:**
  1. Login no sistema com credenciais válidas (`Admin` / `admin123`);
  2. Acesso ao menu “Leave” → “My Leave”;
  3. Seleção de intervalo de datas (Datas fixas para teste de validação: 2025-11-10 a 2025-11-05);
  4. Aplicação do filtro de pesquisa;
  5. Verificação do retorno da página e dos resultados exibidos.

**Resultado esperado:**  
O sistema deve carregar a página corretamente e exibir as licenças correspondentes ao período selecionado.

**Resultado obtido:**  
 **Sucesso.**  
O teste foi executado com uma lógica de asserção aprimorada, verificando a presença de resultados ou a mensagem de erro de validação. O terminal exibiu a mensagem:

> "✅ Search executado — 'No Records Found'." (Resultado esperado para o intervalo de datas escolhido)

**Evidência:**  
Um print do terminal foi anexado ao repositório (`test_date_validation.jpg`), demonstrando o resultado positivo do teste.
Um vídeo do selenuim abrindo o orange e excutando o teste também foi anexado (`test_date_validation.mp4`)

---

### Teste 2 – Reload Leave Page (Complementar)

- **Arquivo:** `test_leave_page_reload.py`
- **Objetivo:** Verificar se o sistema mantém o funcionamento correto da página **Leave** após ser recarregada.
- **Etapas executadas:**
  1. Login no sistema;
  2. Acesso ao menu “Leave”;
  3. Recarregamento da página;
  4. Validação da permanência dos elementos e da funcionalidade.

**Resultado esperado:**  
A página deve ser recarregada sem erros e manter a interface funcional.

**Resultado obtido:**  
 **Sucesso.**  
O terminal exibiu a mensagem:

> “✅ Teste OK: página 'Leave' carregada corretamente!”

**Evidência:**  
Um print do terminal foi anexado ao repositório (`print_page_load_test.jpg`), demonstrando o resultado positivo do teste.

---

## Ambiente de Execução

| Item                        | Descrição                                                  |
| --------------------------- | ---------------------------------------------------------- |
| **Linguagem**               | Python 3                                                   |
| **Biblioteca de automação** | Selenium WebDriver                                         |
| **Navegador utilizado**     | Google Chrome                                              |
| **Driver**                  | ChromeDriver                                               |
| **IDE**                     | VsCode                                                     |
| **Sistema Operacional**     | Windows 10                                                 |
| **Assistência de IA**       | ChatGPT (para download, instalação e execução de comandos) |

---

## Análise dos Resultados

Ambos os testes apresentaram **execução bem-sucedida** e comprovaram o correto funcionamento das principais funcionalidades testadas:

- O teste **My Leave Calendar** validou a **filtragem de solicitações de licença** por intervalo de datas, incluindo uma lógica para verificar a resposta do sistema (resultados ou mensagens de erro/validação).
- O teste **Reload Leave Page** reforçou a **estabilidade e consistência visual** da página mesmo após recarregamentos.

Não foram identificados erros de execução, travamentos ou falhas de carregamento durante os testes.

---

## Conclusão Final

Os testes automatizados desenvolvidos atingiram todos os objetivos propostos:

- O **teste principal** (My Leave Calendar) confirmou o comportamento do sistema ao lidar com intervalos de datas, com asserções explícitas sobre a resposta da aplicação.
- O **teste complementar** (Reload Leave Page) validou a estabilidade da interface do módulo Leave.

Dessa forma, o módulo **Leave** foi considerado **validado com sucesso**, apresentando funcionamento estável e de acordo com os requisitos esperados.

Análise Crítica de Testes Existentes (OrangeHRM)O OrangeHRM é um sistema de Gerenciamento de Recursos Humanos (HRM) amplamente utilizado, inclusive em cursos de teste de software, o que gera uma vasta quantidade de material de terceiros.###1. Testes Disponíveis no Código Original\n\nO código-fonte do OrangeHRM (disponível em `https://github.com/orangehrm/orangehrm`) é uma aplicação complexa e, como esperado de um software de nível empresarial, deve possuir uma suíte de testes internos (unitários, de integração e funcionais) para garantir a qualidade e a estabilidade do produto.

## Análise Crítica:

**Foco:** Os testes internos de um sistema como o OrangeHRM tendem a focar na **cobertura de código** e na **lógica de negócios** (ex: cálculo de licenças, regras de folha de pagamento).

**Qualidade:** A qualidade desses testes é geralmente alta, pois são mantidos pela equipe de desenvolvimento. No entanto, eles são frequentemente escritos para o ambiente de desenvolvimento e podem não ser ideais para testes de aceitação do usuário final.

**Limitação:** O acesso e a execução desses testes internos exigem a configuração completa do ambiente de desenvolvimento (compilação, banco de dados, etc.), o que é inviável para um teste de caixa preta/cinza focado na interface do usuário.\n\n### 2. Material de Terceiros (Comunidade)\n\nA comunidade de testes de software gerou uma grande quantidade de material sobre o OrangeHRM, incluindo:**Casos de Teste Manuais:** Listas de cenários de teste para funcionalidades como escolhidas(ex: `https://www.scribd.com/document/729999012/Test-Cases-for-OrangeHRM`).

**Frameworks de Automação:** Repositórios no GitHub que implementam testes de interface (GUI) usando ferramentas como Selenium, Selenide, e Cypress, focados em módulos específicos (ex: `https://github.com/RaresCode/OrangeHRM`).

**Vantagem:** O material de terceiros é excelente para identificar rapidamente jornadas de usuário e casos de teste de alto nível (testes de sistema/funcionais) que são cruciais para a aceitação.
**Qualidade:** A qualidade varia drasticamente. Enquanto alguns frameworks são robustos e bem estruturados, outros podem ser incompletos, desatualizados ou focados em versões antigas do sistema.

**Risco:** A dependência excessiva de material de terceiros pode levar à duplicação de esforços ou à falha em identificar falhas específicas da versão ou ambiente de teste atual. Além disso, o enunciado proíbe a cópia, exigindo que qualquer fonte seja citada.

## Conclusão da Análise Crítica:

O trabalho desenvolvido (testes automatizados com Selenium) se enquadra na categoria de **Testes de Sistema/Funcionais de Terceiros**, mas com a vantagem de ser **personalizado** para uma jornada de usuário específica (My Leave).Abordagem de focar em um módulo e criar testes de sistema com Selenium é **válida e prática** para a disciplina, pois simula o comportamento do usuário final. A qualidade do teste reside na **escolha dos cenários** e na **robustez das asserções**, como aprimorado na versão corrigida do `my_leave_calendar_test.py`. O ponto fraco é a ausência de testes de níveis mais baixos (unitários/integração), que são cruciais para a cobertura completa, mas difíceis de implementar sem acesso ao código-fonte do sistema.

**Apoio de IA:** Utilizado para configuração do ambiente, assintência para uso dos comandos e refinamento das funções do codigo(especialmente em `my_leave_calendar_test.py`) por ser um teste mais complexo.
