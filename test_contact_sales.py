from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def test_invalid_contact_sales_form():
    driver = webdriver.Chrome()
    driver.get("https://www.orangehrm.com/en/contact-sales")
    driver.maximize_window()

    wait = WebDriverWait(driver, 10)

    
    full_name = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'input[placeholder="Full Name*"]')))
    full_name.clear()
    full_name.send_keys("22")

    
    work_email = driver.find_element(By.CSS_SELECTOR, 'input[placeholder="Work Email*"]')
    work_email.clear()
    work_email.send_keys("teste@example") 

    phone_number = driver.find_element(By.CSS_SELECTOR, 'input[name="Contact"]')
    phone_number.clear()
    phone_number.send_keys("5555555555555555")

    country = driver.find_element(By.CSS_SELECTOR, 'select[name="Country"]')
    country.click()
    country.find_element(By.CSS_SELECTOR, 'option[value="Afghanistan"]').click()

    company_name = driver.find_element(By.CSS_SELECTOR, 'input[name="CompanyName"]')
    company_name.clear()
    company_name.send_keys("Empresa Teste")

    job_title = driver.find_element(By.CSS_SELECTOR, 'input[name="JobTitle"]')
    job_title.clear()
    job_title.send_keys("Tester")

    num_employees = driver.find_element(By.CSS_SELECTOR, 'select[name="NoOfEmployees"]')
    num_employees.click()
    num_employees.find_element(By.CSS_SELECTOR, 'option[value="< 10"]').click()

    message = driver.find_element(By.CSS_SELECTOR, 'textarea[name="Comment"]')
    message.clear()
    message.send_keys("Teste de validação de formulário com dados inválidos.")

    print("Por favor, complete o reCAPTCHA manualmente na janela do navegador.")
    time.sleep(45)

    contact_button = driver.find_element(By.CSS_SELECTOR, 'input[name="action_submitForm"]')
    contact_button.click()

    try:
        email_error = wait.until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, 'span.message.validation'))
        )
        print("Erro detectado na validação do email:", email_error.text)
    except:
        try:
            error_message = wait.until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, '.field-error-message, .error-message'))
            )
            print("Erro detectado na validação do formulário:", error_message.text)
        except:
            print("Nenhuma mensagem de erro detectada. Validação pode estar falhando ou não visível.")

    time.sleep(5)
    driver.quit()

test_invalid_contact_sales_form()