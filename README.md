# OrangeHRM Tests em Go

Este projeto implementa testes de integração para o sistema OrangeHRM usando Go (Golang). O foco é testar as principais funcionalidades da API do OrangeHRM, como autenticação e gerenciamento de funcionários.

## Tecnologias Utilizadas

- **Go (Golang)**: Escolhido por sua simplicidade, performance e excelente suporte para testes
- **Testify**: Framework de asserção para facilitar a escrita de testes
- **godotenv**: Para gerenciamento seguro de variáveis de ambiente
- **net/http**: Biblioteca padrão do Go para requisições HTTP

### Por que Go?

1. **Concorrência Eficiente**: Ideal para testes paralelos
2. **Tipagem Estática**: Ajuda a prevenir erros em tempo de compilação
3. **Ferramentas de Teste Robustas**: Suporte nativo para testes e benchmarks
4. **Simplicidade**: Código limpo e fácil de manter

## Estrutura do Projeto

```
legendary-bassoon/
├── internal/
│   ├── auth/           # Testes de autenticação
│   ├── emplooye/       # Testes de funcionários
│   └── utils/          # Utilitários compartilhados
├── TestData/           # Dados para testes
└── .env                # Configurações de ambiente
```

## Testes Implementados

### 1. Testes de Autenticação
- `TestBuildLoginPayload`: Verifica a construção correta do payload de login
- `TestLoginIntegration`: Testa o processo completo de login na API

### 2. Testes de Funcionários
- `TestEmployeeJourney`: Simula o fluxo completo de adicionar e buscar um funcionário

## Resultados Esperados

### Autenticação
- Login bem-sucedido com credenciais válidas
- Tratamento adequado de erros para credenciais inválidas
- Verificação correta do formato do payload

### Gestão de Funcionários
- Adição bem-sucedida de novos funcionários
- Busca eficiente de funcionários existentes
- Simulação correta das operações da API

## Como Executar os Testes

1. Configure o arquivo `.env` com suas credenciais:
```env
ORANGEHRM_BASE_URL=https://opensource-demo.orangehrmlive.com
ORANGEHRM_USER=Admin
ORANGEHRM_PASS=admin123
```

2. Execute os testes:
```bash
go test ./... -v
```

## Observações

- Os testes de funcionários são simulados devido às limitações da API demo
- O sistema usa variáveis de ambiente para configuração segura
- Todos os testes incluem mensagens descritivas para facilitar a depuração

## Testes UI com Selenium

Adicionei testes de interface que usam Selenium WebDriver (chromedriver) em `internal/ui`.
Por segurança os arquivos de teste UI usam a build tag `ui` e não são executados por padrão.

Passos rápidos para executar os testes UI (Windows PowerShell):

1. Baixe o chromedriver compatível com sua versão do Google Chrome: https://chromedriver.chromium.org/
2. Coloque o `chromedriver.exe` em uma pasta e execute-o (exemplo assume porta 9515):

```powershell
# navegue até a pasta onde está chromedriver.exe
.\chromedriver.exe --port=9515
```

3. Execute os testes UI com a tag `ui`:

```powershell
# roda apenas os testes marcados com //go:build ui
go test -tags=ui ./internal/ui -v
```

Se o chromedriver não estiver rodando, os testes UI serão pulados automaticamente (usamos t.Skip).

Variáveis de ambiente adicionais:

- `SELENIUM_URL`: URL do WebDriver (padrão: http://127.0.0.1:9515)

Observação: os seletores usados nos testes UI são flexíveis (tentamos alguns seletores comuns). Dependendo da versão da interface do OrangeHRM pode ser necessário ajustar os seletores.

### Scripts úteis (PowerShell)

Criei 3 scripts em `scripts/` para tornar fácil baixar o chromedriver e executar os testes:

1. **`install-chromedriver.ps1`**: Detecta a versão do Chrome, baixa o chromedriver compatível e extrai na pasta.

2. **`run-ui-tests.ps1`**: Inicia o chromedriver, executa os testes UI e exibe os resultados no Chrome (deixa o navegador aberto para inspeção).

3. **`open-orangehrm.ps1`**: Abre diretamente o OrangeHRM no Chrome sem rodar testes — perfeito para explorar a interface manualmente.

#### Uso rápido (PowerShell):

```powershell
# 1. Entre na pasta scripts
cd .\scripts

# 2. Baixa e instala o chromedriver (primeira vez)
.\install-chromedriver.ps1

# 3. Escolha uma opção:

# Opção A: Rodar os testes automaticamente
.\run-ui-tests.ps1

# Opção B: Apenas abrir o OrangeHRM no Chrome
.\open-orangehrm.ps1
```

O navegador Chrome abrirá automaticamente. Os testes rodam, fazem login e exibem o resultado no navegador. Você pode inspecionar manualmente antes de encerrar o chromedriver.

Para encerrar o chromedriver após os testes:
- Pressione `Ctrl+C` na janela do PowerShell
- Ou execute: `taskkill /PID <numero> /F` (o número é mostrado na tela)

---
Repositório do semestre anterior:
https://github.com/masmangan/fantastic-octo-eureka
