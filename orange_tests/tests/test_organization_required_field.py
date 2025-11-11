import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

def test_required_field_validation(logged_in_driver):
    driver = logged_in_driver
    wait = WebDriverWait(driver, 10)

    # --- 1. Clicar em Editar ---
    edit_switch = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".oxd-switch-input")))
    driver.execute_script("arguments[0].click();", edit_switch)
    print("Modo de edição ativado.")

    # --- 2. Limpar campo obrigatório ---
    org_name_locator = (By.XPATH, "//label[text()='Organization Name']/parent::div/following-sibling::div/input")
    org_name_input = wait.until(EC.element_to_be_clickable(org_name_locator))
    
    org_name_input.send_keys(Keys.CONTROL + "a")
    org_name_input.send_keys(Keys.DELETE)
    print("Campo 'Organization Name' limpo.")

    # --- 3. Clicar em Salvar ---
    wait.until(EC.invisibility_of_element_located((By.CSS_SELECTOR, ".oxd-form-loader")))
    submit_button = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
    driver.execute_script("arguments[0].click();", submit_button)
    print("Botão 'Salvar' clicado.")

    # --- 4. Verificar a mensagem de erro ---
    # Usar um seletor mais específico para a mensagem de erro do campo
    error_locator = (By.XPATH, "//label[text()='Organization Name']/ancestor::div[contains(@class, 'oxd-input-group')]//span[contains(@class, 'oxd-input-field-error-message')]")
    error_message_element = wait.until(EC.visibility_of_element_located(error_locator))

    # --- 5. Assert (Verificação da Mensagem de Erro) ---
    assert "Required" in error_message_element.text
    print("Teste de validação de campo obrigatório OK.")