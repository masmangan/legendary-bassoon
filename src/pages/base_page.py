from selenium.webdriver.common.by import By

class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def css(self, sel):
        return self.driver.find_element(By.CSS_SELECTOR, sel)

    def x(self, xp):
        return self.driver.find_element(By.XPATH, xp)
