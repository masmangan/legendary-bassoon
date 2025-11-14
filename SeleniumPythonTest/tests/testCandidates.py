import unittest
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time, random

class TestCandidates(unittest.TestCase):
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



    def test_create_reject_delete_candidate(self):
        # Configurações
        USERNAME = "Admin"
        PASSWORD = "admin123"
        WAIT = 10  # segundos para WebDriverWait
        SLEEP = 3  # segundos para time.sleep
        SLEEP_INPUT = 1  # segundos para pausas entre inputs

        # Abrir o navegador Chrome
        driver = self.driver
        driver.maximize_window()
        
        # Login
        username_input = WebDriverWait(driver, WAIT).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "input[placeholder='Username']")))
        username_input.send_keys(USERNAME)

        password_input = driver.find_element(By.CSS_SELECTOR, "input[placeholder='Password']")
        password_input.send_keys(PASSWORD)

        login_button = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
        login_button.click()
        time.sleep(SLEEP)

        # Ir para aba Recruitment
        candidates_button = WebDriverWait(driver, WAIT).until(
            EC.visibility_of_element_located((By.XPATH, "//span[text()='Recruitment']")))
        candidates_button.click()
        time.sleep(SLEEP)

        # Clicar em Add
        add_button = WebDriverWait(driver, WAIT).until(
            EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Add']")))
        add_button.click()
        time.sleep(SLEEP)

        # Lista com 40 nomes individuais
        nomes_unicos = [
            "Lucas", "Mariana", "Rafael", "Beatriz", "Thiago", "Camila", "Gustavo", "Larissa",
            "Felipe", "Ana", "Pedro", "Isabela", "André", "Bianca", "Joao", "Gabriela",
            "Matheus", "Amanda", "Daniel", "Bruna", "Caio", "Leticia", "Eduardo", "Sofia",
            "Rodrigo", "Manuela", "Leonardo", "Clara", "Henrique", "Julia", "Fernando", "Lorena",
            "Vitor", "Marina", "Arthur", "Carolina", "Bruno", "Heloisa", "Diego", "Vitoria"
        ]

        # Dados do candidato
        nome = random.choice(nomes_unicos)
        sobrenome1 = random.choice(nomes_unicos)
        sobrenome2 = random.choice(nomes_unicos)
        #   nome_completo = f"{nome} {sobrenome1} {sobrenome2}"

        # Preencher formulário
        driver.find_element(By.XPATH, "//input[@placeholder='First Name']").send_keys(nome)
        driver.find_element(By.XPATH, "//input[@placeholder='Middle Name']").send_keys(sobrenome1)
        driver.find_element(By.XPATH, "//input[@placeholder='Last Name']").send_keys(sobrenome2)
        driver.find_element(By.XPATH, "(//input[@placeholder='Type here'])[1]").send_keys("email_teste@gmail.com")

        candidate_vacancy_dropdown = WebDriverWait(driver, WAIT).until(
            EC.element_to_be_clickable((By.XPATH, "(//div[@class='oxd-select-text-input'])[1]")))
        candidate_vacancy_dropdown.click()
        time.sleep(SLEEP_INPUT)

        account_option = WebDriverWait(driver, WAIT).until(
            EC.element_to_be_clickable((By.XPATH, "//div[@role='listbox']//span[text()='Junior Account Assistant']")))
        account_option.click()
        time.sleep(SLEEP_INPUT)

        # Cadastrar candidato
        submit_button = driver.find_element(By.XPATH, "//button[@type='submit']")
        submit_button.click()
        time.sleep(SLEEP)

        # Rejeitar candidato
        reject_button = WebDriverWait(driver, WAIT).until(
            EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Reject']")))
        reject_button.click()
        time.sleep(SLEEP_INPUT)

        # Preencher o campo de notes
        notes_input = WebDriverWait(driver, WAIT).until(
            EC.visibility_of_element_located((By.XPATH, "//textarea[@placeholder='Type here']")))
        notes_input.send_keys("candidato ruim")
        time.sleep(SLEEP_INPUT)

        save_button = driver.find_element(By.XPATH, "//button[normalize-space()='Save']")
        save_button.click()
        time.sleep(SLEEP * 1.5)

        # Voltar para aba candidatos
        candidates_button = WebDriverWait(driver, WAIT).until(
            EC.visibility_of_element_located((By.XPATH, "//span[text()='Recruitment']")))
        candidates_button.click()
        time.sleep(SLEEP)

        # Procurar o candidato pelo nome
        search_input = WebDriverWait(driver, WAIT).until(
            EC.visibility_of_element_located((By.XPATH, "//label[text()='Candidate Name']/../following-sibling::div//input")))
        search_input.send_keys(nome)
        time.sleep(SLEEP_INPUT*2)

        # Esperar a lista suspensa aparecer e clicar na primeira opção
        first_suggestion = WebDriverWait(driver, WAIT).until(
            EC.element_to_be_clickable((By.XPATH, "//div[@role='listbox']//div[@role='option'][1]")))
        first_suggestion.click()
        time.sleep(SLEEP_INPUT)

        # Clicar no botão Search
        search_button = driver.find_element(By.XPATH, "//button[normalize-space()='Search']")
        search_button.click()
        time.sleep(SLEEP)

        # Esperar a tabela atualizar e clicar no ícone de lixeira
        delete_icon = WebDriverWait(driver, WAIT).until(
            EC.element_to_be_clickable((By.XPATH, "//i[@class='oxd-icon bi-trash']")))
        delete_icon.click()
        time.sleep(SLEEP_INPUT)

        # Confirmar exclusão no modal
        confirm_delete_button = WebDriverWait(driver, WAIT).until(
            EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Yes, Delete']")))
        confirm_delete_button.click()
        time.sleep(SLEEP)

        try:
            success_message = WebDriverWait(driver, WAIT).until(
                EC.visibility_of_element_located((By.XPATH, "//div[contains(@class, 'oxd-toast--success')]")))
                        
            self.assertTrue(success_message.is_displayed(), "O teste falhou: Mensagem de sucesso não foi exibida.")
                        
        except Exception as e:
            self.fail(f"Não foi possível encontrar a mensagem de sucesso. Erro: {e}")

if __name__ == "__main__":
    unittest.main()