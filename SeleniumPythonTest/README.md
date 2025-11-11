# Automação de Candidatos - OrangeHRM (Selenium Python)

Este script automatiza o processo completo de **criação, rejeição e exclusão de um candidato** no sistema [OrangeHRM Demo](https://opensource-demo.orangehrmlive.com/), utilizando **Python e Selenium WebDriver**.

---

## 🧠 O que o script faz

1. Acessa o OrangeHRM Demo.  
2. Faz login automaticamente com as credenciais padrão (`Admin` / `admin123`).  
3. Acessa a aba **Recruitment**.  
4. Cria um novo candidato com **nomes gerados aleatoriamente**.  
5. Define a vaga “Junior Account Assistant”.  
6. Rejeita o candidato criado, adicionando uma nota (“candidato ruim”).  
7. Retorna à lista de candidatos.  
8. Busca o candidato recém-criado.  
9. Exclui o candidato permanentemente.  
10. Encerra o navegador.



---

## ⚙️ Pré-requisitos

- **Python 3.8+**
- **Google Chrome** (instalado e atualizado)
- **ChromeDriver** compatível com a versão do seu Chrome  
  (ou use `webdriver-manager`, conforme abaixo)
- Biblioteca **Selenium**

Instale os pacotes necessários com:

```bash
pip install -r requirements.txt