import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

# A função de teste recebe 'logged_in_driver' como argumento.
# O Pytest irá automaticamente executar a fixture do conftest.py
def test_update_general_information(logged_in_driver):
    
    driver = logged_in_driver # Apenas renomeando a variável para clareza
    wait = WebDriverWait(driver, 10)
    
    # --- 1. Clicar em Editar --- (Login e navegação já foram feitos)
    edit_switch = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".oxd-switch-input")))
    # Usar clique via JS é mais estável para este tipo de botão "switch"
    driver.execute_script("arguments[0].click();", edit_switch)
    print("Modo de edição ativado.")

    # --- 2. Preparar novos dados ---
    timestamp = str(int(time.time()))
    new_org_name = f"Org Teste {timestamp[-5:]}"
    new_phone = timestamp[-9:]
    print(f"Novos dados: Nome='{new_org_name}', Telefone='{new_phone}'")

    # --- 3. Preencher o formulário ---
    org_name_locator = (By.XPATH, "//label[text()='Organization Name']/parent::div/following-sibling::div/input")
    org_name_input = wait.until(EC.visibility_of_element_located(org_name_locator))
    
    # Limpar campo (CTRL+A, Delete)
    org_name_input.send_keys(Keys.CONTROL + "a")
    org_name_input.send_keys(Keys.DELETE)
    org_name_input.send_keys(new_org_name)

    phone_locator = (By.XPATH, "//label[text()='Phone']/parent::div/following-sibling::div/input")
    phone_input = driver.find_element(*phone_locator)
    phone_input.send_keys(Keys.CONTROL + "a")
    phone_input.send_keys(Keys.DELETE)
    phone_input.send_keys(new_phone)
    print("Formulário preenchido.")

    # --- 4. Salvar ---
    # Adiciona uma espera para o loader desaparecer antes de clicar em salvar
    wait.until(EC.invisibility_of_element_located((By.CSS_SELECTOR, ".oxd-form-loader")))
    driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

    # --- 5. Verificar ---
    # Esperar pelo "toast" de sucesso
    toast_locator = (By.ID, "oxd-toaster_1")
    # A verificação foi melhorada para esperar o texto aparecer no toast,
    # o que é mais robusto do que apenas esperar a visibilidade do container.
    wait.until(EC.text_to_be_present_in_element(toast_locator, "Successfully Updated"))
    print("Mensagem 'Successfully Updated' verificada.")

    # Esperar o toast desaparecer para garantir que a UI não está bloqueada
    wait.until(EC.invisibility_of_element_located(toast_locator))

    # Recarregar a página para garantir que os dados venham do servidor
    print("Recarregando a página para verificar os dados atualizados.")
    driver.refresh()

    # Adicionar uma espera explícita para que o valor seja atualizado no campo
    wait.until(EC.text_to_be_present_in_element_value(org_name_locator, new_org_name))

    # Agora, verificar os valores nos campos desabilitados
    org_name_display = driver.find_element(*org_name_locator).get_attribute("value")
    phone_display = driver.find_element(*phone_locator).get_attribute("value")

    assert org_name_display == new_org_name
    assert phone_display == new_phone
    print("Dados atualizados verificados com sucesso no formulário.")