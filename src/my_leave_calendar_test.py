import unittest
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager


class MyLeaveCalendarTest(unittest.TestCase):

    def setUp(self):
        chrome_options = Options()
        chrome_options.add_argument("--start-maximized")

        # Inicia o navegador
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
        self.driver.get("https://opensource-demo.orangehrmlive.com/")

    def test_date_range_validation(self):
        driver = self.driver
        wait = WebDriverWait(driver, 10)

        # login
        wait.until(EC.presence_of_element_located((By.NAME, "username"))).send_keys("Admin")
        driver.find_element(By.NAME, "password").send_keys("admin123")
        driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

        # aqui espera até o painel carregar
        wait.until(EC.presence_of_element_located((By.XPATH, "//h6[text()='Dashboard']")))

        # navega até o menu Leave
        leave_menu = wait.until(EC.element_to_be_clickable((By.XPATH, "//span[text()='Leave']")))
        leave_menu.click()