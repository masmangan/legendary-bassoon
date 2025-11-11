from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class JobTitlesPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

        self.admin_menu = (By.XPATH, "//span[text()='Admin']")
        self.job_menu = (By.XPATH, "//span[text()='Job ']")
        self.job_titles_option = (By.XPATH, "//a[text()='Job Titles']")
        self.add_button = (By.XPATH, "//button[contains(.,'Add')]")
        self.title_field = (By.XPATH, "//label[contains(text(),'Job Title')]/../following-sibling::div/input")
        self.save_button = (By.XPATH, "//button[contains(.,'Save')]")
        self.search_box = (By.XPATH, "//input[@placeholder='Search']")

    def open_job_titles(self):
        self.wait.until(EC.element_to_be_clickable(self.admin_menu)).click()
        self.wait.until(EC.element_to_be_clickable(self.job_menu)).click()
        self.wait.until(EC.element_to_be_clickable(self.job_titles_option)).click()

    def create_job_title(self, title):
        self.wait.until(EC.element_to_be_clickable(self.add_button)).click()
        self.wait.until(EC.visibility_of_element_located(self.title_field)).send_keys(title)
        self.wait.until(EC.element_to_be_clickable(self.save_button)).click()

    def search_job_title(self, title):
        search = self.wait.until(EC.visibility_of_element_located(self.search_box))
        search.clear()
        search.send_keys(title)

    def job_title_exists(self, title):
        row_xpath = f"//div[contains(@class,'oxd-table-card')]//div[contains(text(),'{title}')]"
        self.wait.until(EC.presence_of_element_located((By.XPATH, row_xpath)))
        return True
