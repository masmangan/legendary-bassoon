from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Abrir o navegador Chrome
driver = webdriver.Chrome()
driver.maximize_window()

driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
time.sleep(3)

# Preencher o campo de username
username_input = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.CSS_SELECTOR, "input[placeholder='Username']")))

username_input.send_keys("Admin")

# Preencher o campo de password
password_input = driver.find_element(By.CSS_SELECTOR, "input[placeholder='Password']")
password_input.send_keys("admin123")

# 5. Clicar no botão de login
login_button = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
login_button.click()

time.sleep(3)

# Navegar para a aba de Admin
admin_button = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.CSS_SELECTOR, "a[href='/web/index.php/admin/viewAdminModule']")))
admin_button.click()
time.sleep(3)

# Clicar no botão Add, que abre o formulário de criaçao de user
add_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Add']")))
add_button.click()

time.sleep(3)

# Preencher o campo de User Role
user_role_dropdown = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "(//div[@class='oxd-select-text-input'])[1]")))
user_role_dropdown.click()
time.sleep(1)

admin_option = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//div[@role='listbox']//span[text()='Admin']")))
admin_option.click()
time.sleep(1)

# Preencher o campo de Emplyee Name
employee_input = driver.find_element(By.XPATH, "//input[@placeholder='Type for hints...']")
employee_input.send_keys("a")
time.sleep(1)

first_employee = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//div[@role='listbox']//span")))
employee_name = first_employee.text
first_employee.click()
time.sleep(1)

# Preencher o campo de status
status_dropdown = driver.find_element(By.XPATH, "(//div[@class='oxd-select-text-input'])[2]")
status_dropdown.click()
time.sleep(1)

enabled_option = driver.find_element(By.XPATH, "//span[text()='Enabled']")
enabled_option.click()
time.sleep(1)

# Preencher o campo de username
username_field = driver.find_element(By.XPATH, "(//input[@class='oxd-input oxd-input--active'])[2]")

import random
unique_username = f"testuser{random.randint(1000, 9999)}"
username_field.send_keys(unique_username)
time.sleep(1)

# Preencher o campo de password
password_field = driver.find_element(By.XPATH, "(//input[@type='password'])[1]")
password_field.send_keys("Test@123")
time.sleep(1)

# Preencher o campo de confirm password
confirm_password_field = driver.find_element(By.XPATH, "(//input[@type='password'])[2]")
confirm_password_field.send_keys("Test@123")
time.sleep(1)

# Clicar no botão Save
save_button = driver.find_element(By.XPATH, "//button[@type='submit']")
save_button.click()
time.sleep(3)

# 8. Verificar mensagem de sucesso
try:
    success_message = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//div[contains(@class, 'oxd-toast--success')]")))
    
    print("\n" + "="*50)
    print("✅ SUCESSO! Usuário criado com sucesso!")
    print(f"✅ Username: {unique_username}")
    print("="*50)
except:
    print("\n❌ ERRO: Mensagem de sucesso não encontrada")
