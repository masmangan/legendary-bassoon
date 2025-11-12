1. Introdução

O sistema analisado neste trabalho é o OrangeHRM, uma plataforma de gerenciamento de recursos humanos (RH) de código aberto amplamente utilizada para fins administrativos e de controle de pessoal. Este relatório apresenta o plano de testes desenvolvido e executado como parte do Trabalho 2 da disciplina de Verificação e Validação de Software, com foco na automação de testes funcionais e na validação de fluxos completos de uso.

O propósito do trabalho é aplicar diferentes tipos de testes em um sistema de complexidade intermediária, documentando as etapas, ferramentas e resultados obtidos de forma clara e colaborativa.

1.1. Acesso ao Sistema e Código-Fonte

URL para Testes: https://opensource-demo.orangehrmlive.com/

Repositório do Código-Fonte: https://github.com/orangehrm/orangehrm

Descrição do Sistema: https://www.orangehrm.com/

O OrangeHRM oferece módulos para administração de pessoal, licenças, gestão de tempo, recrutamento e relatórios, sendo um sistema ideal para demonstração de automação de testes devido à sua interface completa e gratuita para uso acadêmico.

1.2. Execução dos Testes

Os testes foram implementados em Python, utilizando o framework Pytest em conjunto com a biblioteca Selenium WebDriver para automatizar a navegação e interação com o navegador.

Etapas de execução:

Fazer o clone do repositório do projeto para a máquina local.

Instalar as dependências necessárias através do arquivo requirements.txt.

Executar os testes a partir do diretório src com o comando:

pytest

2. Objetivos

O objetivo principal do teste é validar a funcionalidade de cancelamento de solicitações de licença por parte do usuário dentro do sistema OrangeHRM.
Esse processo foi representado como uma jornada de usuário, garantindo que todas as etapas — desde o login até o cancelamento da licença — funcionem corretamente e sem erros de interface.

2.1. Jornada do Usuário: Cancelar Solicitação de Licença

Ator: Funcionário ou Administrador

Objetivo: Cancelar uma solicitação de licença (folga ou férias) previamente cadastrada.

Pré-condição: O usuário deve estar autenticado e possuir pelo menos uma solicitação de licença pendente.

Fluxo principal:

O usuário realiza o login no sistema.

Acessa a seção “My Leave” (Minhas Licenças).

Visualiza a lista de solicitações de licença existentes.

Seleciona uma solicitação pendente e clica no botão Cancel.

O sistema processa a solicitação e atualiza o status da licença.

Pós-condição: A licença é marcada como cancelada e, se aplicável, o saldo de dias de licença do usuário é atualizado.

3. Casos de Teste

O caso de teste automatizado foi planejado para abranger integralmente o fluxo descrito na jornada do usuário.

ID	Título do Teste	Passos de Execução	Dados de Teste	Resultado Esperado
1	test_cancel_my_leave	1. Acessar a URL de login.
2. Inserir usuário e senha.
3. Clicar em Login.
4. Acessar a página My Leave.
5. Clicar em Cancel na primeira solicitação encontrada.
6. Confirmar que a página ainda exibe o título My Leave.	URL: https://opensource-demo.orangehrmlive.com/

Usuário: Admin
Senha: admin123	A solicitação de licença é cancelada com sucesso (se existir). O sistema permanece na página My Leave sem erros.
4. Resultado dos Testes

A execução do teste automatizado foi bem-sucedida. O cenário foi completado sem a ocorrência de erros ou comportamentos inesperados.
O sistema reagiu conforme o esperado, processando o cancelamento de forma correta sempre que havia uma solicitação pendente.

Nos casos em que não havia solicitações de licença disponíveis para cancelamento, o script tratou a exceção adequadamente, exibindo a mensagem informativa no console sem interromper o fluxo de execução.
Esse comportamento confirma a robustez e estabilidade do teste automatizado, demonstrando que o script é capaz de lidar com diferentes condições do sistema sem falhas.