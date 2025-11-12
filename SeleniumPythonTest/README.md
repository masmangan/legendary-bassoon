# Plano de Testes: Criação de Novo Usuário

## Introdução

Este plano de testes contempla o sistema OrangeHRM, focado no fluxo de criação, rejeição e exclusão de um candidato*através do módulo Recruitment.

O teste foi implementado em Python utilizando a biblioteca Selenium WebDriver para automatizar todo o processo de criação de um novo candidato, rejeição do mesmo e exclusão final do registro.


## Desenvolvimento do trabalho

Na primeira etapa, realizei a navegação pelo sistema OrangeHRM para compreender as funcionalidades disponíveis e identificar fluxos de teste possíveis. Após essa análise, escolhi o fluxo de Rejeição e Exclusão de Candidato, por envolver múltiplas etapas do sistema e ser um bom caso de teste automatizado.

Na sequência, elaborei o **README.md** com o plano de testes, descrevendo os objetivos, casos de teste, entradas e resultados esperados antes de iniciar a codificação.

Nas aulas seguintes, desenvolvi o script de automação utilizando o Selenium, baseado no exemplo de login fornecido em aulas anteriores. O código foi refinado até contemplar as seguintes ações:
- Login automático no sistema;
- Criação de um candidato com dados aleatórios;
- Rejeição do candidato com justificativa;
- Busca e exclusão do candidato no sistema.


## Como executar

### 1. Instale as dependências

Certifique-se de estar na pasta do projeto:
```bash
pip install -r requirements.txt
# deve conter selenium e outras dependências necessárias
```

### 2. Execute o teste

Para criação de novo usuário:
```bash
python3 tests/testCandidates.py
```

##  Objetivos

1. Acessar o site do OrangeHRM;
2. Realizar login com as credenciais padrão (Admin / admin123);
3. Navegar até o módulo Recruitment;
4. Clicar em Add para abrir o formulário de criação de candidato;
5. Preencher o formulário com nome, sobrenomes e e-mail gerados automaticamente;
6. Selecionar a vaga “Junior Account Assistant”;
7. Clicar em Save para cadastrar o candidato;
8. Clicar em Reject e preencher o campo de notes com uma justificativa;
9. Salvar a rejeição;
10. Retornar à aba de candidatos;
11. Buscar o candidato recém-criado pelo nome;
12. Clicar no ícone de lixeira para excluir o registro;
13. Confirmar a exclusão no modal.
14. Encerra o navegador


## Casos de Teste

### Rejeitar e excluir candidato criado automaticamente:

**Cenário:** Criar, rejeitar e excluir um candidato usando Selenium.

**Entradas:** 
- Nome, Sobrenome 1, Sobrenome 2: Gerados aleatoriamente a partir de uma lista com 40 nomes únicos
- Vaga: “Junior Account Assistant”
- Nota de rejeição: “candidato ruim”
- E-mail: “email_teste@gmail.com”

**Passos:** Login → Recruitment → Add → Preencher formulário → Save → Reject → Notes → Save → Buscar candidato → Delete → Confirm Delete

**Resultado Esperado:** O candidato é criado com sucesso, rejeitado e posteriormente excluído do sistema. Ao final da execução, o terminal exibe uma mensagem confirmando a exclusão com sucesso.


## Execução dos Testes

### Ambiente de teste:

- **Sistema:** Windows 11
- **Python:** 3.11.7
- **Navegador:** Google Chrome
- **Biblioteca de automação:** Selenium
- **Método de execução:** linha de comando via terminal PowerShell ou Bash


## Resultados dos testes

### Rejeitar e excluir candidato:

**Resultado:** Passou 

**Observações:** 

1. O candidato foi criado, rejeitado e excluído com sucesso, conforme o esperado.
2. O uso de nomes aleatórios garante que cada execução seja única e evite conflitos com registros existentes.
3. Em caso de lentidão do site, o teste pode falhar por tempo limite — nesse caso, recomenda-se aumentar o tempo de WAIT ou SLEEP.


**Conclusão:** 

O teste automatizado cumpre com sucesso o objetivo proposto, validando o fluxo de Rejeição e Exclusão de Candidatos dentro do sistema OrangeHRM Demo.
A automação se mostrou estável, reutilizável e bem estruturada para futuras expansões de testes relacionados ao módulo de recrutamento.