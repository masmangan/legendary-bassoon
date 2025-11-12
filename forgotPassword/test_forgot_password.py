# -*- coding: utf-8 -*-
import time
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

BASE_URL = "https://opensource-demo.orangehrmlive.com/"

@pytest.fixture
def driver():
    opts = Options()
    opts.add_argument("--start-maximized")
    drv = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=opts)
    drv.implicitly_wait(5)
    yield drv
    drv.quit()

def test_forgot_password_envia_confirmacao(driver):
    # realiza o login
    driver.get(BASE_URL)
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "username")))

    # vai pra aba de esqueceu a senha
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//p[contains(.,'Forgot your password')]"))
    ).click()

    # tela de resetar a senha
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//h6[normalize-space(.)='Reset Password']"))
    )
    user = driver.find_element(By.NAME, "username")
    user.clear()
    user.send_keys("Admin")

    # envia o email pra recuperar senha
    driver.find_element(
        By.XPATH, "//button[@type='submit' and normalize-space(.)='Reset Password']"
    ).click()

    # valida, aqui ele aceita o toast ou o card de sucesso, como o app nao retorna o email, ele aceita o toast e encerra
    elem = wait.until(EC.any_of(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "div.oxd-toast")),  # toast
        EC.visibility_of_element_located((
            By.XPATH, "//h6[contains(normalize-space(.),'Link para resetar a senha foi enviado ao e-mail')]"
        )),  # título do card
    ))

    # texto de ok
    page_ok = "Reset Password link sent successfully" in (elem.text or "") \
              or "sendPasswordReset" in driver.current_url \
              or "Reset Password link sent successfully" in driver.page_source
    assert page_ok, "Mensagem de sucesso não encontrada."

    driver.save_screenshot("print.png")
    time.sleep(1)
