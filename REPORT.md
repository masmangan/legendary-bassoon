# Relatório da Suíte de Testes Automatizados do OrangeHRM - Julian F. R. V. Silveira

## Visão Geral

Esta suíte de testes automatiza a verificação do aplicativo de demonstração **OrangeHRM** usando o **Playwright para Python**.  
A suíte consiste em **três testes principais** que verificam a navegação básica, a autenticação de usuários e a modificação de perfil.

---

## Estrutura da Suíte de Testes

### Casos de Teste

#### 1. `test_navigation_to_website()`

**Propósito:** Verificar a navegação bem-sucedida até a página de login do OrangeHRM.

**Ações:**

- Inicia o navegador Chromium  
- Navega até a página de login do OrangeHRM  
- Aguarda o carregamento completo da página  
- Verifica se o título da página é **"OrangeHRM"**

**Critério de Sucesso:** O título da página corresponde a "OrangeHRM".  
**Artefatos:** Captura de tela salva em `./test_prints/test_navigation_to_website/` com carimbo de data/hora.

---

#### 2. `test_login()`

**Propósito:** Testar a autenticação de usuário com credenciais válidas.

**Ações:**

- Navega até a página de login  
- Preenche o nome de usuário ("Admin") e senha ("admin123")  
- Clica no botão de login  
- Aguarda a conclusão da navegação  

**Critério de Sucesso:** A URL contém "dashboard", indicando login bem-sucedido.  
**Artefatos:** Captura de tela salva em `./test_prints/test_login/` com carimbo de data/hora.

---

#### 3. `test_change_user_name()`

**Propósito:** Testar a modificação de perfil alterando o primeiro e o último nome do usuário.

**Ações:**

- Faz login no aplicativo  
- Navega até a página **"My Info"** via barra lateral  
- Atualiza o primeiro nome para "James" e o sobrenome para "Queue"  
- Salva as alterações usando o botão secundário  
- Retorna ao painel principal e verifica a exibição do nome atualizado  

**Critério de Sucesso:** O menu do usuário exibe **"James Queue"**.  
**Artefatos:** Captura de tela salva em `./test_prints/test_change_user_name/` com carimbo de data/hora.

---

## Implementação Técnica

### Dependências

- **Playwright:** Framework de automação de navegador  
- **Python 3.7+:** Ambiente de execução  
- **Chromium:** Motor de navegador (instalado automaticamente pelo Playwright)

---

## Estrutura de Arquivos

```
jfrvs/
    └──src/
        └──test.py
    ├──README.md
    ├──REPORT.md
    ├──requirements.py
    ├──setup.sh
    └──LICENSE
```

---

## Configuração e Instalação

### Pré-requisitos

- Python 3.7 ou superior  
- pip (gerenciador de pacotes Python)  
- Git (para controle de versão)

### Etapas de Instalação

1. Instale as dependências:

```bash
pip install -r requirements.txt
playwright install
playwright install-deps
```

2. Alternativamente, use o script de instalação `setup.sh`:

```bash
#!/bin/bash
echo "Instalando dependências Python..."
pip install -r requirements.txt

echo "Instalando navegadores Playwright..."
playwright install

echo "Instalando dependências do sistema..."
playwright install-deps

echo "Configuração concluída com sucesso!"
```

Torne o script executável e execute:

```bash
chmod +x setup.sh
./setup.sh
```

---

## Execução dos Testes

### Executar toda a suíte:

```bash
python jfrvs/src/test.py
```

**Saída Esperada:**

```
==================================================
Primeiro teste: Navegação
==================================================
Iniciando Chromium...
Navegando para OrangeHRM...
Passou!
==================================================
Segundo teste: Acesso
==================================================
Iniciando Chromium...
Navegando para OrangeHRM...
Preenchendo credenciais...
Fazendo login...
Passou!
==================================================
Terceiro teste: Alterando nome do usuário
==================================================
Iniciando Chromium...
Navegando para OrangeHRM...
Preenchendo credenciais...
Fazendo login...
James Queue
Passou!
==================================================
Resultados: 3 de 3 testes executados com sucesso.
==================================================
```

## Dados de Teste

**Credenciais:**  
- Nome de usuário: `Admin`  
- Senha: `admin123`  

**Dados do Usuário de Teste:**  
- Primeiro Nome: `James`  
- Sobrenome: `Queue`

---

## Funcionalidades e Boas Práticas

### ✅ Funcionalidades Implementadas

- **Automação em modo headless:** usando Playwright com Chromium  
- **Verificação visual:** capturas de tela com carimbo de data/hora  
- **Seleção robusta de elementos:** via seletores CSS e estratégias de espera adequadas  
- **Registro estruturado:** saída de console clara e separada por teste  
- **Tratamento de erros:** limpeza adequada do navegador com blocos `try-finally`

### ✅ Qualidade do Código

- **Design modular:** funções separadas para cada caso de teste  
- **Gerenciamento de constantes:** configuração centralizada de URLs  
- **Gerenciamento de recursos:** encerramento correto das instâncias de navegador  
- **Saída legível:** progresso dos testes claramente indicado

---

## Solução de Problemas

### Problemas Comuns

**Instalação do Navegador:**  
```bash
playwright install
```

**Instalação de Dependências:**  
```bash
pip install --upgrade pip
pip install -r requirements.txt
```

**Diretório de Capturas:**  
Certifique-se de que os subdiretórios dentro de `test_prints` existam ou sejam criados automaticamente.

**Problemas de Rede:**  
- Verifique a conexão com a internet  
- Confirme se o site de demonstração do OrangeHRM está acessível

### Modo de Depuração

Para depurar, altere o modo de inicialização do navegador para modo visível:

```python
browser = p.chromium.launch(headless=False)  # Mude para False para visualizar o navegador
```

---

## Manutenção

### Atualizações Regulares

- Atualize o Playwright periodicamente para novos recursos e correções de segurança  
- Monitore alterações na interface do OrangeHRM que possam afetar seletores  
- Revise e atualize as credenciais de teste conforme necessário

### Extensão da Suíte

Novos testes podem ser adicionados seguindo o padrão existente:

1. Crie uma nova função de teste  
2. Implemente a navegação e as ações necessárias  
3. Adicione a lógica de verificação  
4. Inclua no bloco principal de execução

---

## Conclusão

Esta suíte de testes fornece uma base sólida para automação de testes do OrangeHRM.  
O design modular permite fácil manutenção e extensão, enquanto o registro detalhado e as capturas de tela facilitam a depuração e a verificação dos resultados.
