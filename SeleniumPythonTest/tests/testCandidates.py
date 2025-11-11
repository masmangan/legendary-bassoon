
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import time
import uuid

# Configurações
BASE_URL = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"
USERNAME = "Admin"
PASSWORD = "admin123"
WAIT = 10  # segundos para WebDriverWait
SLEEP = 3  # segundos para time.sleep
SLEEP_INPUT = 1  # segundos para pausas entre inputs

# Abrir o navegador Chrome
driver = webdriver.Chrome()
driver.maximize_window()

driver.get(BASE_URL)
time.sleep(SLEEP)

# Preencher o campo de username
username_input = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.CSS_SELECTOR, "input[placeholder='Username']")))

username_input.send_keys(USERNAME)

# Preencher o campo de password
password_input = driver.find_element(By.CSS_SELECTOR, "input[placeholder='Password']")
password_input.send_keys(PASSWORD)

# Clicar no botão de login
login_button = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
login_button.click()

time.sleep(SLEEP)

# Navegar para a aba de candidatos
candidates_button = WebDriverWait(driver, WAIT).until(
    EC.visibility_of_element_located((By.XPATH, "//span[text()='Recruitment']")))
candidates_button.click()
time.sleep(SLEEP)


# Clicar no botão Add, que abre o formulário de criaçao de candidato
add_button = WebDriverWait(driver, WAIT).until(
    EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Add']")))
add_button.click()

time.sleep(SLEEP)

# Preencher o campo de nome
nome_field = driver.find_element(By.XPATH, "//input[@placeholder='First Name']")
nome_field.send_keys("teste")
time.sleep(SLEEP_INPUT)

sobrenome1_field = driver.find_element(By.XPATH, "//input[@placeholder='Middle Name']")
sobrenome1_field.send_keys("sobrenome1")
time.sleep(SLEEP_INPUT)

sobrenome2_field = driver.find_element(By.XPATH, "//input[@placeholder='Last Name']")
sobrenome2_field.send_keys("sobrenome2")
time.sleep(SLEEP_INPUT)


# Preencher o campo de User Role
candidate_vacancy_dropdown = WebDriverWait(driver, WAIT).until(
    EC.element_to_be_clickable((By.XPATH, "(//div[@class='oxd-select-text-input'])[1]")))
candidate_vacancy_dropdown.click()
time.sleep(SLEEP_INPUT)

admin_option = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//div[@role='listbox']//span[text()='Junior Account Assistant']")))
admin_option.click()
time.sleep(SLEEP_INPUT)


# Preencher o campo de email
employee_input = driver.find_element(By.XPATH, "(//input[@placeholder='Type here'])[1]")
employee_input.send_keys("email_teste@gmail.com")
time.sleep(SLEEP_INPUT)


# Clicar no botão Save
save_button = driver.find_element(By.XPATH, "//button[@type='submit']")
save_button.click()
time.sleep(SLEEP)

# Clicar no botão de Shortlist
#   shortlist_button = WebDriverWait(driver, WAIT).until(
#       EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Shortlist']")))
#   shortlist_button.click()
#   time.sleep(SLEEP)

# Clicar no botão de reject
#   reject_button = driver.find_element(By.XPATH, "//button[normalize-space()='Reject']")
#   reject_button.click()
#   time.sleep(SLEEP)

# Preencher o campo de notes
#   notes_input = driver.find_element(By.XPATH, "//input[@placeholder='Type here']")
#   if(reject_button is not None):
#       notes_input.send_keys("candidato rejeitado")
#   else:
#       notes_input.send_keys("bom candidato")
#   time.sleep(SLEEP_INPUT)