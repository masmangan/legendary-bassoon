from selenium.webdriver.common.by import By
from .BasePage import BasePage
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from datetime import timedelta
import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException


class PIMPage(BasePage):
    """Page Object para a página PIM (Employee List) do OrangeHRM."""

    # Localizadores
    PIM_MENU_LINK = (By.XPATH, "//span[text()='PIM']")
    EMPLOYEE_LIST_LINK = (By.XPATH, "//a[text()='Employee List']")
    EMPLOYEE_NAME_INPUT = (By.XPATH, "(//input[@placeholder='Type for hints...'])[1]")
    SEARCH_BUTTON = (By.XPATH, "//button[@type='submit']")
    NO_RECORDS_MESSAGE = (By.XPATH, "//span[text()='No Records Found']")
    RESULTS_TABLE = (By.XPATH, "//div[@class='oxd-table-body']")
    SPINNER = (By.XPATH, "//div[@class='oxd-loading-spinner']")

    def __init__(self, driver):
        super().__init__(driver)

    def navigate_to_employee_list(self):
        """Navega até o menu PIM e abre a lista de funcionários (robusto mesmo com overlays)."""
        print("🔄 Aguardando o menu PIM aparecer...")

        time.sleep(4)  # tempo de renderização pós-login

        # tenta várias abordagens progressivas
        for attempt in range(3):
            try:
                pim_element = self.driver.find_element(By.XPATH, "//span[normalize-space()='PIM']")
                self.driver.execute_script("arguments[0].scrollIntoView(true);", pim_element)
                time.sleep(0.5)
                self.driver.execute_script("arguments[0].click();", pim_element)
                print("✅ Menu PIM clicado via JavaScript!")
                break
            except (NoSuchElementException, ElementClickInterceptedException):
                print(f"⚠️ Tentativa {attempt+1}: elemento ainda não disponível, tentando novamente...")
                time.sleep(2)
        else:
            raise TimeoutError("❌ Não foi possível clicar no menu PIM após 3 tentativas.")

        time.sleep(2)
        try:
            emp_link = self.driver.find_element(By.XPATH, "//a[normalize-space()='Employee List']")
            self.driver.execute_script("arguments[0].click();", emp_link)
            print("✅ Página Employee List acessada com sucesso!")
        except Exception:
            raise TimeoutError("❌ Link 'Employee List' não encontrado.")

        self.wait_for_url_contains("/web/index.php/pim/viewEmployeeList")
        print("✅ Navegação para Employee List confirmada!")

    def search_employee(self, employee_name):
        """Digita o nome e realiza a busca."""
        name_input = self.wait_for_element_visibility(self.EMPLOYEE_NAME_INPUT)

        name_input.clear()
        name_input.send_keys(employee_name)
        
        self.driver.find_element(*self.SEARCH_BUTTON).click()
        
        # Espera que o spinner de carregamento desapareça para garantir que a busca foi concluída
        self.wait_for_element_invisibility(self.SPINNER)
        
        print(f"🔍 Busca realizada para: {employee_name}")

    def has_search_results(self):
        """Verifica se há resultados na tabela."""
        try:
            WebDriverWait(self.driver, 5).until(
                lambda driver: len(driver.find_elements(*self.RESULTS_TABLE)) > 0
            )
            return len(self.driver.find_elements(*self.RESULTS_TABLE)) > 0
        except TimeoutException:
            return False

    def is_no_records_message_displayed(self):
        """Verifica se a mensagem 'No Records Found' é exibida."""
        try:
            self.wait_for_element_visibility(self.NO_RECORDS_MESSAGE)
            return True
        except TimeoutException:
            return False
