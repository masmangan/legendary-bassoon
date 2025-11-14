import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC
import time


class CreateUserTest(unittest.TestCase):

    def setUp(self):
        try:
            # Tenta rodar com interface gráfica (local)
            chrome_options = Options()
            chrome_options.add_argument("--start-maximized")
            chrome_options.add_argument("--disable-extensions")
            
            self.driver = webdriver.Chrome(options=chrome_options)
            print("Chrome iniciado com interface gráfica (modo local)")

        except Exception as e:
            print(f"Não foi possível iniciar Chrome com interface gráfica: {e}")
            print("Iniciando Chrome em modo headless (Codespaces/CI)...")
            
            # Modo headless para ambientes sem interface gráfica
            chrome_options = Options()
            chrome_options.add_argument("--headless")
            chrome_options.add_argument("--no-sandbox")
            chrome_options.add_argument("--disable-dev-shm-usage")
            chrome_options.add_argument("--disable-gpu")
            chrome_options.add_argument("--window-size=1920,1080")
            chrome_options.add_argument("--disable-extensions")
            chrome_options.add_argument("--disable-software-rasterizer")

            self.driver = webdriver.Chrome(options=chrome_options)
            print("Chrome iniciado em modo headless com sucesso")

        self.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        time.sleep(3)


    def tearDown(self):
        self.driver.quit()


    def test_createUser(self):
        driver = self.driver

        # Preencher o campo de username
        username_input = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.NAME, "username")))
        username_input.send_keys("Admin")

        # Preencher o campo de password
        password_input = driver.find_element(By.NAME, "password")
        password_input.send_keys("admin123")

        # Clicar no botão de login
        login_button = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
        login_button.click()
        print("Login realizado com sucesso.")
        time.sleep(3)

        # Navegar para a aba de Admin
        admin_button = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "a[href='/web/index.php/admin/viewAdminModule']")))
        admin_button.click()
        print("Navegado para o módulo Admin.")
        time.sleep(3)

        # Clicar no botão Add, que abre o formulário de criaçao de user
        add_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='button'].oxd-button--medium.oxd-button--secondary")))
        add_button.click()
        print("Clicado no botão 'Add' para abrir o formulário de criação.")
        time.sleep(3)

        # Preencher o campo de User Role
        user_role_dropdown = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "(//div[@class='oxd-select-text-input'])[1]")))
        user_role_dropdown.click()
        time.sleep(1)

        admin_option = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//div[@role='listbox']//span[text()='Admin']")))
        admin_option.click()
        print("Definido User Role: Admin.")
        time.sleep(3)

        # Preencher o campo de Employee Name
        employee_input = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//label[text()='Employee Name']/../following-sibling::div//input"))
        )        
        employee_input.send_keys("a")
        time.sleep(1)

        first_employee = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//div[@role='listbox']//span")))
        first_employee.click()
        print("Selecionado Employee Name.")
        time.sleep(1)

        # Preencher o campo de status
        status_dropdown = driver.find_element(By.XPATH, "(//div[@class='oxd-select-text-input'])[2]")
        status_dropdown.click()
        time.sleep(1)

        enabled_option = driver.find_element(By.XPATH, "//span[text()='Enabled']")
        enabled_option.click()
        print("Definido Status: Enabled.")
        time.sleep(1)

        # Preencher o campo de username
        username_field = driver.find_element(By.XPATH, "(//input[@class='oxd-input oxd-input--active'])[2]")

        import random
        unique_username = f"testuser{random.randint(1000, 9999)}"
        username_field.send_keys(unique_username)
        print(f"Definido Username único: {unique_username}.")
        time.sleep(1)

        # Preencher o campo de password
        password_field = driver.find_element(By.XPATH, "(//input[@type='password'])[1]")
        password_field.send_keys("Test@123")
        time.sleep(1)

        # Preencher o campo de confirm password
        confirm_password_field = driver.find_element(By.XPATH, "(//input[@type='password'])[2]")
        confirm_password_field.send_keys("Test@123")
        print("Senhas preenchidas.")
        time.sleep(1)

        # Clicar no botão Save
        save_button = driver.find_element(By.XPATH, "//button[@type='submit']")
        print("Clicado no botão 'Save' para submeter o formulário.")
        save_button.click()
        time.sleep(3)

        # Verificar mensagem de sucesso ou erro
        try:
            success_message = WebDriverWait(driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, "//div[contains(@class, 'oxd-toast--success')]")))
            
            self.assertTrue(success_message.is_displayed(), "O teste falhou: Mensagem de sucesso não foi exibida.")
            
        except Exception as e:
            self.fail(f"Não foi possível encontrar a mensagem de sucesso. Erro: {e}")


if __name__ == "__main__":
    unittest.main()
