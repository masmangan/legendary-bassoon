from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Configurações
BASE_URL = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"
USERNAME = "Admin"
PASSWORD = "admin123"
WAIT = 10     # segundos para WebDriverWait
SLEEP = 2     # segundos de pausa padrão

# Inicializar navegador
driver = webdriver.Chrome()
driver.maximize_window()
driver.get(BASE_URL)
time.sleep(SLEEP)

try:
    # ===== LOGIN =====
    username_input = WebDriverWait(driver, WAIT).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "input[placeholder='Username']"))
    )
    username_input.send_keys(USERNAME)

    password_input = driver.find_element(By.CSS_SELECTOR, "input[placeholder='Password']")
    password_input.send_keys(PASSWORD)

    login_button = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
    login_button.click()
    time.sleep(SLEEP)

    # Verificar se login foi bem-sucedido
    dashboard_element = WebDriverWait(driver, WAIT).until(
        EC.visibility_of_element_located((By.XPATH, "//h6[text()='Dashboard']"))
    )
    print("\n Login realizado com sucesso!")

    # ===== LOGOUT =====
    user_dropdown = WebDriverWait(driver, WAIT).until(
        EC.element_to_be_clickable((By.CLASS_NAME, "oxd-userdropdown-name"))
    )
    user_dropdown.click()
    time.sleep(SLEEP)

    logout_button = WebDriverWait(driver, WAIT).until(
        EC.element_to_be_clickable((By.XPATH, "//a[text()='Logout']"))
    )
    logout_button.click()
    time.sleep(SLEEP)

    # Verificar se logout funcionou
    login_header = WebDriverWait(driver, WAIT).until(
        EC.visibility_of_element_located((By.XPATH, "//h5[text()='Login']"))
    )
    print("Logout realizado com sucesso!")

except Exception as e:
    print(f"\n Erro durante o teste: {e}")

finally:
    driver.quit()
    print("\n Teste finalizado.")
