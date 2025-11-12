from selenium.webdriver.common.by import By
from .BasePage import BasePage

class LoginPage(BasePage):
    """Page Object para a página de Login do OrangeHRM."""

    # Localizadores
    USERNAME_INPUT = (By.NAME, "username")
    PASSWORD_INPUT = (By.NAME, "password")
    LOGIN_BUTTON = (By.XPATH, "//button[@type='submit']")
    DASHBOARD_URL_PART = "/web/index.php/dashboard/index"

    def __init__(self, driver):
        super().__init__(driver)

    def login(self, username, password):
        """Realiza o login no sistema."""
        print("? Tentando fazer login...")
        
        # Espera e preenche o campo de usuário
        username_field = self.wait_for_element_visibility(self.USERNAME_INPUT)
        username_field.send_keys(username)

        # Espera e preenche o campo de senha
        password_field = self.wait_for_element_visibility(self.PASSWORD_INPUT)
        password_field.send_keys(password)

        # Clica no botão de login
        login_button = self.wait_for_element_clickable(self.LOGIN_BUTTON)
        login_button.click()
        print("? Botão de login clicado. Aguardando carregamento...")

        # Espera a URL do dashboard para confirmar o login
        self.wait_for_url_contains(self.DASHBOARD_URL_PART)
        
        # Localizador para o cabeçalho "Dashboard" (elemento que só aparece após o carregamento completo)
        DASHBOARD_HEADER = (By.XPATH, "//h6[text()='Dashboard']")
        self.wait_for_element_visibility(DASHBOARD_HEADER)
        
        print("? Página carregada completamente após o login!")
