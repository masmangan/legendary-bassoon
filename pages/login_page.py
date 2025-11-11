from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)
        self.username = (By.NAME, "username")
        self.password = (By.NAME, "password")
        self.login_button = (By.CSS_SELECTOR, "button[type='submit']")

    def login(self, user, pwd):
        self.wait.until(EC.visibility_of_element_located(self.username)).send_keys(user)
        self.wait.until(EC.visibility_of_element_located(self.password)).send_keys(pwd)
        self.wait.until(EC.element_to_be_clickable(self.login_button)).click()
        self.wait.until(EC.url_contains("dashboard"))
