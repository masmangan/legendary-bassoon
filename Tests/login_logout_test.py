from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

"""
Jornada de Usuário - Login/Logout

1. Acessar página de login.
2. Inserir usuário.
3. Inserir senha.
4. Clicar em Login.
5. Validar chegada ao Dashboard.
6. Abrir menu do usuário.
7. Clicar em Logout.
8. Validar retorno à página de login.
"""

# Configurações
BASE_URL = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"
USERNAME = "Admin"
PASSWORD = "admin123"
WAIT = 10
SLEEP = 2

driver = webdriver.Chrome()
driver.get(BASE_URL)
driver.maximize_window()
time.sleep(SLEEP)

try:
    # LOGIN
    username_input = WebDriverWait(driver, WAIT).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "input[placeholder='Username']"))
    )
    username_input.send_keys(USERNAME)

    password_input = driver.find_element(By.CSS_SELECTOR, "input[placeholder='Password']")
    password_input.send_keys(PASSWORD)

    login_button = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
    login_button.click()

    # ASSERT LOGIN
    dashboard_title = WebDriverWait(driver, WAIT).until(
        EC.visibility_of_element_located((By.XPATH, "//h6[text()='Dashboard']"))
    )
    assert dashboard_title.is_displayed(), "ERRO: Dashboard não apareceu após login!"

    print(" Login validado com assert.")

    # LOGOUT
    user_dropdown = WebDriverWait(driver, WAIT).until(
        EC.element_to_be_clickable((By.CLASS_NAME, "oxd-userdropdown-name"))
    )
    user_dropdown.click()

    logout_button = WebDriverWait(driver, WAIT).until(
        EC.element_to_be_clickable((By.XPATH, "//a[text()='Logout']"))
    )
    logout_button.click()

    # ASSERT LOGOUT
    login_title = WebDriverWait(driver, WAIT).until(
        EC.visibility_of_element_located((By.XPATH, "//h5[text()='Login']"))
    )
    assert login_title.is_displayed(), "ERRO: Tela de login não apareceu após logout!"

    print(" Logout validado com assert.")

except Exception as e:
    print(f" Erro durante o teste: {e}")

finally:
    driver.quit()
    print("Teste finalizado.")
