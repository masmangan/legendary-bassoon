Este repositório apresenta um projeto de testes automatizados desenvolvido para o sistema OrangeHRM, como parte da avaliação da disciplina Verificação e Validação de Software.

1. Visão Geral do Projeto

O principal objetivo deste trabalho é demonstrar a aplicação de testes automatizados de ponta a ponta (E2E) em um sistema web. A automação foi desenvolvida em Python, utilizando a biblioteca Selenium para simular a navegação e interação de um usuário real com o sistema OrangeHRM, dentro de um cenário prático e específico.

2. Sistema Sob Teste

Sistema: OrangeHRM (Open Source Human Resource Management)

URL: https://opensource-demo.orangehrmlive.com/

Descrição: Plataforma voltada à gestão de recursos humanos, com módulos para administração de pessoal, controle de licenças, gerenciamento de tempo, recrutamento, entre outros.

3. Execução dos Testes
3.1. Pré-requisitos

Python 3.x instalado.

Gerenciador de pacotes pip configurado.

Navegador Google Chrome e o ChromeDriver compatível com a versão instalada do navegador, devidamente incluído no PATH do sistema.

3.2. Instalação

Faça o clone deste repositório em sua máquina local.

Acesse a pasta src e instale as dependências do projeto com o comando adequado do pip.

3.3. Execução

Dentro do diretório src, execute o Pytest.
O framework identificará automaticamente os arquivos de teste e realizará a execução.

Para gerar um relatório em HTML, utilize o plugin pytest-html (como demonstrado no arquivo report.html incluído).

4. Cenário de Teste Implementado

O teste automatizado desenvolvido cobre o seguinte cenário:

Título: Cancelar uma solicitação de licença em My Leave.

Descrição: O script realiza o login na aplicação, acessa a seção My Leave e tenta cancelar a primeira solicitação de licença pendente disponível. O teste é considerado bem-sucedido se o processo ocorre sem falhas na interface, independentemente de existir ou não uma solicitação efetivamente cancelada.

Arquivo: src/leave_cancel_test.py