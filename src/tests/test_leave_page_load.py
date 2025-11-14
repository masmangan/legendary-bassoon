import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LeavePageTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

    def test_leave_page_load(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        wait.until(EC.presence_of_element_located((By.NAME, "username"))).send_keys("Admin")
        driver.find_element(By.NAME, "password").send_keys("admin123")
        driver.find_element(By.XPATH, "//button[@type='submit']").click()

        dashboard_header = wait.until(EC.presence_of_element_located(
            (By.XPATH, "//h6[contains(., 'Dashboard') or contains(., 'Tablero')]")
        ))
        self.assertTrue(dashboard_header.is_displayed(), "❌ Falha: Dashboard não carregado após login")

        leave_tab = wait.until(EC.element_to_be_clickable(
            (By.XPATH, "//span[contains(., 'Leave') or contains(., 'Licencias') or contains(., 'Permisos')]")
        ))
        leave_tab.click()

        from_date_label = wait.until(EC.presence_of_element_located((
            By.XPATH,
            "//label[contains(., 'From Date') or contains(., 'Desde') or contains(., 'De')]"
        )))
        self.assertTrue(from_date_label.is_displayed(), "❌ Falha: página 'Leave' não carregou corretamente")

        print("✅ Teste OK: página 'Leave' carregada corretamente!")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
