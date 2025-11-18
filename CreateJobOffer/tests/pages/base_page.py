"""
Classe base para todos os Page Objects
"""
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains
from ..config import config


class BasePage:
    """Classe base para todos os Page Objects"""
    
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, config.EXPLICIT_WAIT)
        self.actions = ActionChains(driver)
    
    def find_element(self, locator):
        """Encontra um elemento na página"""
        try:
            return self.wait.until(EC.presence_of_element_located(locator))
        except TimeoutException:
            raise NoSuchElementException(f"Elemento não encontrado: {locator}")
    
    def find_elements(self, locator):
        """Encontra múltiplos elementos na página"""
        return self.wait.until(EC.presence_of_all_elements_located(locator))
    
    def click(self, locator):
        """Clica em um elemento"""
        element = self.wait.until(EC.element_to_be_clickable(locator))
        element.click()
    
    def type_text(self, locator, text):
        """Digite texto em um campo"""
        element = self.find_element(locator)
        element.clear()
        element.send_keys(text)
    
    def get_text(self, locator):
        """Obtém o texto de um elemento"""
        element = self.find_element(locator)
        return element.text
    
    def is_element_visible(self, locator, timeout=None):
        """Verifica se um elemento está visível"""
        try:
            wait = WebDriverWait(self.driver, timeout or config.EXPLICIT_WAIT)
            wait.until(EC.visibility_of_element_located(locator))
            return True
        except TimeoutException:
            return False
    
    def is_element_present(self, locator):
        """Verifica se um elemento está presente no DOM"""
        try:
            self.driver.find_element(*locator)
            return True
        except NoSuchElementException:
            return False
    
    def wait_for_page_load(self):
        """Aguarda o carregamento completo da página"""
        self.wait.until(
            lambda driver: driver.execute_script("return document.readyState") == "complete"
        )
    
    def scroll_to_element(self, locator):
        """Faz scroll até o elemento"""
        element = self.find_element(locator)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
    
    def select_dropdown_option_by_text(self, locator, text):
        """Seleciona uma opção de dropdown pelo texto visível"""
        # Clica no dropdown
        self.click(locator)
        # Aguarda as opções aparecerem e seleciona pelo texto
        from selenium.webdriver.common.by import By
        option_locator = (By.XPATH, f"//*[contains(text(), '{text}')]")
        self.click(option_locator)
    
    def get_current_url(self):
        """Retorna a URL atual"""
        return self.driver.current_url
    
    def refresh_page(self):
        """Atualiza a página"""
        self.driver.refresh()

