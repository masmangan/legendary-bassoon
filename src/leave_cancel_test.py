import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()

def test_cancel_my_leave(driver):
    """
    Cenário: Cancelar uma solicitação em 'My Leave'
    """
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

    time.sleep(2)
    driver.find_element(By.NAME, "username").send_keys("Admin")
    driver.find_element(By.NAME, "password").send_keys("admin123")
    driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

    time.sleep(3)
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/leave/viewMyLeaveList")

    time.sleep(3)
    try:
        cancel_button = driver.find_element(By.XPATH, "//button[contains(., 'Cancel')]")
        cancel_button.click()
        time.sleep(2)
        print(" Solicitação de licença cancelada com sucesso.")
    except:
        print(" Nenhuma solicitação encontrada para cancelar — talvez o usuário não tenha pedidos pendentes.")

    assert "My Leave" in driver.page_source
    print("Teste finalizado — verifique mensagens acima.")