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

Implementei um **teste de sistema** (end-to-end) automatizado usando Selenium e Python.

* **Tecnologia:** Selenium WebDriver com Python.
* **Cenário:** O script `createUserTest.py` automatiza o "Fluxo Principal" descrito acima.
* **Robustez:** O script utiliza `WebDriverWait` para lidar com esperas dinâmicas (elementos que demoram a carregar), evitando que o teste falhe por lentidão da página.
* **Dado de Teste:** O *username* é gerado aleatoriamente (`testuserXXXX`) para garantir que o teste possa ser executado várias vezes sem conflito de usuário existente.

## Setup para o teste

### Pré-requisitos

Para executar este teste, você precisará ter o **Python** instalado, juntamente com a biblioteca do **Selenium** e um **WebDriver** compatível com seu navegador.

1.  **Instale a biblioteca do Selenium:**
    ```bash
    pip install selenium
    ```


### Como executar

Após configurar os pré-requisitos, basta executar o script Python:

```bash
python createUserTest.py
```
