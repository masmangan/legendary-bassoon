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

---
Repositório do semestre anterior:
https://github.com/masmangan/fantastic-octo-eureka
