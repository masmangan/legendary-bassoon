# Relatório – Teste Automatizado com Selenium

## Desenvolvimento do Teste Automatizado

Na **primeira aula**, observei os testes automatizados produzidos pelos alunos do semestre passado. A partir dessa análise, escolhi qual fluxo eu iria implementar neste trabalho.

Na **segunda aula**, utilizei como base um código de login desenvolvido por um aluno do semestre anterior. Adaptei esse código ao meu próprio projeto. Além disso, implementei todo o restante da automação: criação de um novo usuário a partir do painel administrativo, realização de logout, login com o usuário recém-criado e, por fim, a publicação de um post na área **“Buzz”** do sistema.

---

## Descrição do Teste Automatizado

O teste implementado consiste nos seguintes passos:

1. Logar no sistema como **Admin**.  
2. Acessar o módulo **Admin** e criar um **novo usuário**.  
3. Realizar **logout** da conta administrativa.  
4. Logar no sistema utilizando o **usuário recém-criado**.  
5. Acessar o módulo **Buzz** e **publicar uma mensagem**.

Esse fluxo verifica tanto funcionalidades administrativas quanto o comportamento comum de um usuário final.

---

## Setup Necessário para Execução

### Criar o ambiente virtual:

```
python -m venv venv
```

### Ativar o ambiente virtual:

Linux/macOS:
```
source venv/bin/activate
```

Windows:
```
venv\Scripts\Activate
```

### Instalar o Selenium:

```
pip install selenium
```

### Executar o teste:

```
python t2.py
```

---

## Explicação do Fluxo do Código

O código é organizado em funções que refletem as etapas reais da utilização do sistema:

- **login()** – acessa a página de autenticação, insere usuário e senha e aguarda o carregamento do painel administrativo.  
- **create_user()** – dentro do módulo Admin, abre o formulário de criação, preenche os dados do novo usuário e confirma.  
- **logout()** – abre o menu do usuário logado e efetua a saída do sistema.  
- **post_on_buzz()** – acessa a área Buzz, localiza o campo de postagem e envia a mensagem desejada.  
- **run_flow()** – função principal que organiza o fluxo completo do teste, executando cada etapa na ordem correta.  

O uso de **WebDriverWait** garante que todos os elementos estejam visíveis ou clicáveis antes da interação, evitando falhas por carregamento lento da interface.

---

## Código Completo do Teste

```python
BASE_URL = "https://opensource-demo.orangehrmlive.com"

def wait_clickable(driver, by, sel, timeout=15):
    return WebDriverWait(driver, timeout).until(EC.element_to_be_clickable((by, sel)))

def wait_visible(driver, by, sel, timeout=15):
    return WebDriverWait(driver, timeout).until(EC.visibility_of_element_located((by, sel)))

def login(driver, username, password):
    driver.get(f"{BASE_URL}/web/index.php/auth/login}")
    wait_visible(driver, By.CSS_SELECTOR, 'input[placeholder="Username"]').clear()
    driver.find_element(By.CSS_SELECTOR, 'input[placeholder="Username"]').send_keys(username)
    driver.find_element(By.CSS_SELECTOR, 'input[placeholder="Password"]').clear()
    driver.find_element(By.CSS_SELECTOR, 'input[placeholder="Password"]').send_keys(password)
    driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()
    wait_visible(driver, By.CSS_SELECTOR, "aside.oxd-sidepanel")

def logout(driver):
    wait_clickable(driver, By.CSS_SELECTOR, "span.oxd-userdropdown-tab").click()
    wait_clickable(driver, By.XPATH, "//a[normalize-space()='Logout']").click()
    wait_visible(driver, By.CSS_SELECTOR, 'input[placeholder="Username"]')

def open_admin_users_page(driver):
    wait_clickable(driver, By.XPATH, "//span[normalize-space()='Admin']").click()
    wait_visible(driver, By.XPATH, "//button[.//i[contains(@class,'bi-plus')]]")

def create_user(driver, employee_name, new_username, new_password, role_text="Admin", status_text="Enabled"):
    open_admin_users_page(driver)

    wait_clickable(driver, By.XPATH, "//button[.//i[contains(@class,'bi-plus')]]").click()

    select_dropdown_by_label(driver, "User Role", role_text)
    select_dropdown_by_label(driver, "Status", status_text)

    emp_input = wait_visible(driver, By.XPATH, "//label[normalize-space()='Employee Name']/../following-sibling::div//input")
    emp_input.clear()
    emp_input.send_keys(employee_name)
    wait_clickable(driver, By.XPATH, f"//div[@role='listbox']//span[contains(normalize-space(), '{employee_name.split()[0]}')]").click()

    user_input = wait_visible(driver, By.XPATH, "//label[normalize-space()='Username']/../following-sibling::div//input")
    user_input.clear()
    user_input.send_keys(new_username)

    pwd_input = wait_visible(driver, By.XPATH, "//label[normalize-space()='Password']/../following-sibling::div//input[@type='password']")
    pwd_input.clear()
    pwd_input.send_keys(new_password)

    conf_input = wait_visible(driver, By.XPATH, "//label[normalize-space()='Confirm Password']/../following-sibling::div//input[@type='password']")
    conf_input.clear()
    conf_input.send_keys(new_password)

    wait_clickable(driver, By.XPATH, "//button[normalize-space()='Save']").click()

    wait_visible(driver, By.XPATH, "//h5[normalize-space()='System Users']")

def post_on_buzz(driver, message_text):
    wait_clickable(driver, By.XPATH, "//span[normalize-space()='Buzz']").click()

    text_area = wait_visible(driver, By.XPATH, "//textarea[@placeholder=\"What's on your mind?\"]")
    text_area.click()
    text_area.send_keys(message_text)

    wait_clickable(driver, By.XPATH, "//button[@type='submit' and normalize-space()='Post']").click()

    wait_visible(driver, By.XPATH, f"//p[contains(normalize-space(), '{message_text}')]")

def run_flow():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(0)

    admin_user = "Admin"
    admin_pass = "admin123"
    new_user = "testeT2usuario3"
    new_pass = "Senha@123"
    employee = "Ranga Akunuri"
    buzz_msg = "Ola mundo"

    try:
        login(driver, admin_user, admin_pass)
        create_user(driver, employee, new_user, new_pass, role_text="ESS", status_text="Enabled")
        logout(driver)
        login(driver, new_user, new_pass)
        post_on_buzz(driver, buzz_msg)
        time.sleep(2)

    finally:
        driver.quit()

if __name__ == "__main__":
    run_flow()
```

