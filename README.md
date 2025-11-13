# Projeto de Verificação e Validação de Software

Este repositório contém um trabalho de Verificação e Validação de Software, utilizando o OrangeHRM Open-source como base para fazer testes de integração.

O trabalho foi desenvolvido com o auxílio das seguintes ferramentas:
*   Selenium IDE
*   Gemini

## Teste

### `addLogEmployee.java`

Este teste de integração verifica a funcionalidade de adicionar um registro de log de desempenho para um funcionário no OrangeHRM.

O fluxo do teste é o seguinte:
1.  **Login:** Acessa a aplicação com credenciais de administrador.
2.  **Navegação:** Vai para a seção "Performance", e depois para "Employee Trackers".
3.  **Seleção:** Escolhe um tracker de funcionário existente na lista.
4.  **Adicionar Log:** Clica no botão "Add Log" para iniciar a criação de um novo registro.
5.  **Preenchimento:** adiciona um título para o log e um comentário descritivo.
6.  **Submissão:** Salva o novo registro de log.
7.  **Verificação:** Confirma se o novo log foi adicionado com sucesso e está visível na página de trackers do funcionário.
8.  **Logout:** Encerra a sessão do usuário.

O objetivo deste teste é garantir que o fluxo para adicionar um feedback de desempenho a um funcionário está funcionando como devia.