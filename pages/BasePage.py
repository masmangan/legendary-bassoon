from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from datetime import timedelta

class BasePage:
    """Classe base para todas as Page Objects, contendo métodos comuns."""

    def __init__(self, driver: WebDriver):
        self.driver = driver
        # Explicit Wait de 20 segundos para máxima estabilidade
        self.wait = WebDriverWait(self.driver, 30, poll_frequency=0.5)

    def wait_for_element_visibility(self, locator):
        """Espera até que o elemento esteja visível."""
        try:
            return self.wait.until(EC.visibility_of_element_located(locator))
        except TimeoutException:
            raise TimeoutException(f"Timeout: Elemento não visível: {locator}")

    def wait_for_element_clickable(self, locator):
        """Espera até que o elemento esteja clicável."""
        try:
            return self.wait.until(EC.element_to_be_clickable(locator))
        except TimeoutException:
            raise TimeoutException(f"Timeout: Elemento não clicável: {locator}")

    def wait_for_url_contains(self, url_part):
        """Espera até que a URL contenha a parte especificada."""
        try:
            self.wait.until(EC.url_contains(url_part))
        except TimeoutException:
            raise TimeoutException(f"Timeout: URL não contém: {url_part}")

    def wait_for_element_invisibility(self, locator):
        """Espera até que o elemento esteja invisível."""
        try:
            self.wait.until(EC.invisibility_of_element_located(locator))
        except TimeoutException:
            raise TimeoutException(f"Timeout: Elemento não ficou invisível: {locator}")
