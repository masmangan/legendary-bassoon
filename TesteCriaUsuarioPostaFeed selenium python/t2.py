from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time



BASE_URL = "https://opensource-demo.orangehrmlive.com"

def wait_clickable(driver, by, sel, timeout=15):
    return WebDriverWait(driver, timeout).until(EC.element_to_be_clickable((by, sel)))

def wait_visible(driver, by, sel, timeout=15):
    return WebDriverWait(driver, timeout).until(EC.visibility_of_element_located((by, sel)))

def select_dropdown_by_label(driver, label_text, option_text):
    field = wait_clickable(
        driver,
        By.XPATH,
        f"//label[normalize-space()='{label_text}']/../following-sibling::div//div[contains(@class,'oxd-select-text')]"
    )
    field.click()

    wait_clickable(
        driver,
        By.XPATH,
        f"//div[@role='listbox']//*[self::span or self::div][normalize-space()='{option_text}']"
    ).click()

    # valida seleção
    selected = wait_visible(
        driver,
        By.XPATH,
        f"//label[normalize-space()='{label_text}']/../following-sibling::div//div[contains(@class,'oxd-select-text-input')]"
    ).text.strip()
    assert selected.lower() == option_text.lower(), f"{label_text} ficou '{selected}', esperava '{option_text}'"


def login(driver, username, password):
    driver.get(f"{BASE_URL}/web/index.php/auth/login")
    wait_visible(driver, By.CSS_SELECTOR, 'input[placeholder="Username"]').clear()
    driver.find_element(By.CSS_SELECTOR, 'input[placeholder="Username"]').send_keys(username)
    driver.find_element(By.CSS_SELECTOR, 'input[placeholder="Password"]').clear()
    driver.find_element(By.CSS_SELECTOR, 'input[placeholder="Password"]').send_keys(password)
    driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()
    wait_visible(driver, By.CSS_SELECTOR, "aside.oxd-sidepanel")

def logout(driver):
    wait_clickable(driver, By.CSS_SELECTOR, "span.oxd-userdropdown-tab").click()
    wait_clickable(driver, By.XPATH, "//a[normalize-space()='Logout']").click()
    wait_visible(driver, By.CSS_SELECTOR, 'input[placeholder="Username"]')

def open_admin_users_page(driver):
    wait_clickable(driver, By.XPATH, "//span[normalize-space()='Admin']").click()
    wait_visible(driver, By.XPATH, "//button[.//i[contains(@class,'bi-plus')]]")

def create_user(driver, employee_name, new_username, new_password, role_text="Admin", status_text="Enabled"):
    open_admin_users_page(driver)

    wait_clickable(driver, By.XPATH, "//button[.//i[contains(@class,'bi-plus')]]").click()

    select_dropdown_by_label(driver, "User Role", role_text)

    select_dropdown_by_label(driver, "Status", status_text)

    emp_input = wait_visible(driver, By.XPATH, "//label[normalize-space()='Employee Name']/../following-sibling::div//input")
    emp_input.clear()
    emp_input.send_keys(employee_name)
    wait_clickable(driver, By.XPATH, f"//div[@role='listbox']//span[contains(normalize-space(), '{employee_name.split()[0]}')]").click()

    user_input = wait_visible(driver, By.XPATH, "//label[normalize-space()='Username']/../following-sibling::div//input")
    user_input.clear()
    user_input.send_keys(new_username)

    pwd_input = wait_visible(driver, By.XPATH, "//label[normalize-space()='Password']/../following-sibling::div//input[@type='password']")
    pwd_input.clear()
    pwd_input.send_keys(new_password)

    conf_input = wait_visible(driver, By.XPATH, "//label[normalize-space()='Confirm Password']/../following-sibling::div//input[@type='password']")
    conf_input.clear()
    conf_input.send_keys(new_password)

    wait_clickable(driver, By.XPATH, "//button[normalize-space()='Save']").click()

    wait_visible(driver, By.XPATH, "//h5[normalize-space()='System Users']")

def post_on_buzz(driver, message_text):
    wait_clickable(driver, By.XPATH, "//span[normalize-space()='Buzz']").click()

    time.sleep(2)
    text_area = wait_visible(driver, By.XPATH, "//textarea[@placeholder=\"What's on your mind?\"]")
    text_area.click()
    text_area.send_keys(message_text)

    wait_clickable(driver, By.XPATH, "//button[@type='submit' and normalize-space()='Post']").click()

    wait_visible(driver, By.XPATH, f"//p[contains(normalize-space(), '{message_text}')]")
    time.sleep(2)


def run_flow():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(0)  

    admin_user = "Admin"
    admin_pass = "admin123"
    new_user = "testeT2usuario7"
    new_pass = "Senha@123"
    employee = "Ranga Akunuri"
    buzz_msg = "Ola mundo"

    teste_passou = False 

    try:
        # 1) Login como Admin
        login(driver, admin_user, admin_pass)

        # 2) Criar usuario
        create_user(driver, employee, new_user, new_pass, role_text="ESS", status_text="Enabled")

        # 3) Logout Admin
        logout(driver)

        # 4) Login com o usuario criado
        login(driver, new_user, new_pass)

        # 5) Postar no Buzz
        post_on_buzz(driver, buzz_msg)

        

        assert buzz_msg in driver.page_source, "Mensagem final não encontrada no Buzz"

        teste_passou = True  

    except Exception as e:
        print(f"[ERRO] O teste falhou: {e}")

    finally:
        driver.quit()
        if teste_passou:
            print("\n Teste passou com sucesso!\n")
        else:
            print("\n Teste falhou\n")
        
         

if __name__ == "__main__":
    run_flow()
