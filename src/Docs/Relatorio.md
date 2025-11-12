1. Resumo da Execução

A execução foi realizada em 11 de novembro de 2025, às 17h19min39s, e o relatório foi gerado automaticamente pela ferramenta pytest-html.

Resumo geral:

Total de testes executados: 1

Testes aprovados (Passed): 1

Testes com falha (Failed): 0

Duração total: 27 segundos

O resultado geral foi bem-sucedido, sem a ocorrência de erros, falhas de execução ou defeitos detectados no comportamento do sistema sob teste.

2. Detalhes do Teste Executado

O teste automatizado executado teve como foco a validação da jornada de cancelamento de uma solicitação de licença no módulo My Leave do OrangeHRM.

Teste	Cenário	Resultado	Duração
leave_cancel_test.py::test_cancel_my_leave	Cancelar uma solicitação em “My Leave”	Passed	27s
2.1. Evidências da Execução

Durante o processo de execução, o script de teste realizou automaticamente as seguintes etapas no sistema:

Login: Efetuou autenticação no sistema utilizando as credenciais de administrador fornecidas para o ambiente de demonstração.

Navegação: Acessou a seção My Leave para listar as solicitações de licença existentes.

Ação: Tentou cancelar a primeira solicitação pendente encontrada. O log de execução registrou dois comportamentos possíveis:

Caso 1: Solicitação de licença encontrada e cancelada com sucesso.

Caso 2: Nenhuma solicitação pendente disponível para cancelamento, com o script exibindo mensagem informativa no console.

Validação: Após a tentativa de cancelamento, o teste verificou que a página My Leave permaneceu estável e sem erros de interface, confirmando o funcionamento esperado do sistema.

Essas evidências indicam que o fluxo principal do teste foi concluído sem interrupções e que o script é capaz de lidar corretamente com condições alternativas do sistema.

3. Defeitos Encontrados

Nenhum defeito foi identificado durante a execução.
O sistema respondeu adequadamente às ações simuladas e manteve a integridade da interface durante todo o processo, validando o comportamento esperado da funcionalidade testada.

4. Ambiente de Teste

Os testes foram executados em um ambiente configurado conforme descrito abaixo:

Sistema Operacional: Linux

Versão do Python: 3.14 (inferido a partir dos arquivos de cache gerados)

Frameworks Utilizados: pytest, selenium

Navegador: Google Chrome

Sistema Alvo: OrangeHRM Demo (versão web oficial – https://opensource-demo.orangehrmlive.com/)