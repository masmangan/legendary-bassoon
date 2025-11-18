"""
Page Object para a página de Login do Orange HRM
"""
from selenium.webdriver.common.by import By
from .base_page import BasePage
from ..config import config


class LoginPage(BasePage):
    """Page Object para a página de login"""
    
    # Locators
    USERNAME_INPUT = (By.NAME, "username")
    PASSWORD_INPUT = (By.NAME, "password")
    LOGIN_BUTTON = (By.XPATH, "//button[@type='submit']")
    ERROR_MESSAGE = (By.XPATH, "//p[contains(@class, 'oxd-alert-content-text')]")
    DASHBOARD_HEADER = (By.XPATH, "//h6[text()='Dashboard']")
    
    def __init__(self, driver):
        super().__init__(driver)
        self.url = f"{config.BASE_URL}/web/index.php/auth/login"
    
    def open(self):
        """Abre a página de login"""
        self.driver.get(self.url)
        self.wait_for_page_load()
    
    def login(self, username, password):
        """Realiza o login no sistema"""
        self.type_text(self.USERNAME_INPUT, username)
        self.type_text(self.PASSWORD_INPUT, password)
        self.click(self.LOGIN_BUTTON)
        # Aguarda redirecionamento para o dashboard
        self.is_element_visible(self.DASHBOARD_HEADER)
    
    def is_login_successful(self):
        """Verifica se o login foi bem-sucedido"""
        return self.is_element_visible(self.DASHBOARD_HEADER)
    
    def get_error_message(self):
        """Obtém a mensagem de erro de login"""
        if self.is_element_visible(self.ERROR_MESSAGE, timeout=5):
            return self.get_text(self.ERROR_MESSAGE)
        return None

