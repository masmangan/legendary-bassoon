# Explicação do teste de Criação de Usuário no sistema 

Este documento descreve os testes automatizados para a funcionalidade de **criação de usuário** no sistema Orange HRM. Os testes cobrem o fluxo completo desde o login até a verificação da criação bem-sucedida do usuário.


### Fluxo Principal

1. Realizar login no sistema com credenciais de administrador
2. Acessar o menu "Admin" na sidebar lateral esquerda
3. Clicar no botão "Add" para adicionar novo usuário
4. Preencher o formulário com as informações do usuário:
   - **User Role**: Papel do usuário (Admin, ESS)
   - **Employee Name**: Nome do funcionário (autocomplete)
   - **Status**: Status do usuário (Enabled/Disabled)
   - **Username**: Nome de usuário único
   - **Password**: Senha forte
   - **Confirm Password**: Confirmação da senha
5. Clicar no botão "Save"
6. Verificar mensagem de sucesso


## O que eu fiz?

- 

## Setup para o teste

### Como executar 

## Código:

