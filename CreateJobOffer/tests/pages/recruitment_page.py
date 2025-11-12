"""
Page Object para o módulo de Recrutamento do Orange HRM
"""
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from .base_page import BasePage
from ..config import config
import time


class RecruitmentPage(BasePage):
    """Page Object para a página de Recrutamento"""
    
    # Locators - Menu
    RECRUITMENT_MENU = (By.XPATH, "//span[text()='Recruitment']")
    VACANCIES_TAB = (By.XPATH, "//a[text()='Vacancies']")
    
    # Locators - Lista de Vagas
    ADD_BUTTON = (By.XPATH, "//button[contains(., 'Add')]")
    VACANCY_LIST = (By.XPATH, "//div[@class='oxd-table-body']")
    SEARCH_VACANCY_INPUT = (By.XPATH, "//label[text()='Vacancy']/following::input[1]")
    SEARCH_BUTTON = (By.XPATH, "//button[@type='submit' and contains(., 'Search')]")
    
    # Locators - Formulário de Criação de Vaga
    VACANCY_NAME_INPUT = (By.XPATH, "//label[text()='Vacancy Name']/following::input[1]")
    JOB_TITLE_DROPDOWN = (By.XPATH, "//label[text()='Job Title']/following::div[1]//i")
    DESCRIPTION_TEXTAREA = (By.XPATH, "//label[text()='Description']/following::textarea[1]")
    HIRING_MANAGER_INPUT = (By.XPATH, "//label[text()='Hiring Manager']/following::input[1]")
    NUMBER_OF_POSITIONS_INPUT = (By.XPATH, "//label[text()='Number of Positions']/following::input[1]")
    ACTIVE_CHECKBOX = (By.XPATH, "//label[text()='Active']/following::span[1]")
    PUBLISH_IN_RSS_CHECKBOX = (By.XPATH, "//label[text()='Publish in RSS feed and web page']/following::span[1]")
    
    # Locators - Botões do Formulário
    SAVE_BUTTON = (By.XPATH, "//button[@type='submit']")
    CANCEL_BUTTON = (By.XPATH, "//button[@type='button' and contains(., 'Cancel')]")
    
    # Locators - Mensagens
    SUCCESS_MESSAGE = (By.XPATH, "//p[contains(@class, 'oxd-text--toast-message')]")
    ERROR_MESSAGE = (By.XPATH, "//span[contains(@class, 'oxd-input-field-error-message')]")
    
    # Locators - Tabela de Resultados
    TABLE_ROWS = (By.XPATH, "//div[@class='oxd-table-card']")
    NO_RECORDS_MESSAGE = (By.XPATH, "//span[text()='No Records Found']")
    
    def __init__(self, driver):
        super().__init__(driver)
        self.url = f"{config.BASE_URL}/web/index.php/recruitment/viewJobVacancy"
    
    def navigate_to_recruitment(self):
        """Navega para o módulo de Recrutamento"""
        self.click(self.RECRUITMENT_MENU)
        time.sleep(2)  # Aguarda menu expandir/navegar
    
    def navigate_to_vacancies(self):
        """Navega para a página de Vagas"""
        # Abordagem mais direta: navegar pela URL
        self.driver.get(self.url)
        time.sleep(2)
        self.wait_for_page_load()
        
        # Verificar se chegamos na página correta (botão Add deve estar visível)
        if not self.is_element_visible(self.ADD_BUTTON, timeout=5):
            # Se não funcionou pela URL, tentar pelo menu
            try:
                self.click(self.RECRUITMENT_MENU)
                time.sleep(2)
                
                # Tentar clicar na aba Vacancies se existir
                if self.is_element_visible(self.VACANCIES_TAB, timeout=2):
                    self.click(self.VACANCIES_TAB)
                    time.sleep(2)
            except:
                pass
    
    def click_add_vacancy(self):
        """Clica no botão para adicionar nova vaga"""
        self.click(self.ADD_BUTTON)
        time.sleep(1)  # Aguarda formulário carregar
    
    def fill_vacancy_name(self, name):
        """Preenche o nome da vaga"""
        self.type_text(self.VACANCY_NAME_INPUT, name)
    
    def select_job_title(self, job_title):
        """Seleciona o cargo da vaga"""
        self.click(self.JOB_TITLE_DROPDOWN)
        time.sleep(0.5)
        option_locator = (By.XPATH, f"//div[@role='option']//span[text()='{job_title}']")
        self.click(option_locator)
    
    def fill_description(self, description):
        """Preenche a descrição da vaga"""
        self.type_text(self.DESCRIPTION_TEXTAREA, description)
    
    def select_hiring_manager(self, manager_name):
        """Seleciona o gerente de contratação"""
        self.type_text(self.HIRING_MANAGER_INPUT, manager_name)
        time.sleep(2)  # Aguarda autocomplete carregar
        # Seleciona primeira opção do autocomplete
        option_locator = (By.XPATH, f"//div[@role='option']//span[contains(text(), '{manager_name}')]")
        time.sleep(0.5)
        self.click(option_locator)
        time.sleep(0.5)  # Aguarda seleção confirmar
    
    def fill_number_of_positions(self, number):
        """Preenche o número de posições"""
        self.type_text(self.NUMBER_OF_POSITIONS_INPUT, str(number))
    
    def set_active_status(self, is_active=True):
        """Define o status ativo da vaga"""
        checkbox = self.find_element(self.ACTIVE_CHECKBOX)
        is_checked = "oxd-checkbox-input--active" in checkbox.get_attribute("class")
        
        if is_active and not is_checked:
            self.click(self.ACTIVE_CHECKBOX)
        elif not is_active and is_checked:
            self.click(self.ACTIVE_CHECKBOX)
    
    def set_publish_in_rss(self, publish=True):
        """Define se a vaga será publicada no RSS"""
        checkbox = self.find_element(self.PUBLISH_IN_RSS_CHECKBOX)
        is_checked = "oxd-checkbox-input--active" in checkbox.get_attribute("class")
        
        if publish and not is_checked:
            self.click(self.PUBLISH_IN_RSS_CHECKBOX)
        elif not publish and is_checked:
            self.click(self.PUBLISH_IN_RSS_CHECKBOX)
    
    def click_save(self):
        """Clica no botão Salvar"""
        # Scroll até o botão e aguardar estar clicável
        self.scroll_to_element(self.SAVE_BUTTON)
        time.sleep(0.5)
        self.click(self.SAVE_BUTTON)
        time.sleep(3)  # Aguarda processamento e mensagens
    
    def click_cancel(self):
        """Clica no botão Cancelar"""
        self.click(self.CANCEL_BUTTON)
    
    def create_vacancy(self, vacancy_data):
        """
        Cria uma nova vaga com os dados fornecidos
        
        Args:
            vacancy_data: dict contendo os dados da vaga
                - vacancy_name (str): Nome da vaga
                - job_title (str): Cargo
                - description (str): Descrição
                - hiring_manager (str): Nome do gerente
                - number_of_positions (str/int): Número de posições
                - is_active (bool, optional): Status ativo
                - publish_in_rss (bool, optional): Publicar no RSS
        """
        self.fill_vacancy_name(vacancy_data['vacancy_name'])
        self.select_job_title(vacancy_data['job_title'])
        self.fill_description(vacancy_data['description'])
        self.select_hiring_manager(vacancy_data['hiring_manager'])
        self.fill_number_of_positions(vacancy_data['number_of_positions'])
        
        if 'is_active' in vacancy_data:
            self.set_active_status(vacancy_data['is_active'])
        
        if 'publish_in_rss' in vacancy_data:
            self.set_publish_in_rss(vacancy_data['publish_in_rss'])
        
        self.click_save()
    
    def is_success_message_displayed(self):
        """Verifica se a mensagem de sucesso é exibida"""
        return self.is_element_visible(self.SUCCESS_MESSAGE, timeout=5)
    
    def get_success_message(self):
        """Obtém o texto da mensagem de sucesso"""
        if self.is_success_message_displayed():
            return self.get_text(self.SUCCESS_MESSAGE)
        return None
    
    def get_error_messages(self):
        """Obtém todas as mensagens de erro do formulário"""
        try:
            error_elements = self.find_elements(self.ERROR_MESSAGE)
            return [elem.text for elem in error_elements]
        except:
            return []
    
    def search_vacancy(self, vacancy_name):
        """Busca uma vaga pelo nome"""
        self.type_text(self.SEARCH_VACANCY_INPUT, vacancy_name)
        self.click(self.SEARCH_BUTTON)
        time.sleep(2)  # Aguarda resultados
    
    def is_vacancy_in_list(self, vacancy_name):
        """Verifica se uma vaga está na lista de resultados"""
        try:
            vacancy_locator = (By.XPATH, f"//div[contains(text(), '{vacancy_name}')]")
            return self.is_element_visible(vacancy_locator, timeout=5)
        except:
            return False
    
    def get_vacancy_count(self):
        """Retorna o número de vagas na lista"""
        try:
            rows = self.find_elements(self.TABLE_ROWS)
            return len(rows)
        except:
            return 0
    
    def is_no_records_message_displayed(self):
        """Verifica se a mensagem 'No Records Found' é exibida"""
        return self.is_element_visible(self.NO_RECORDS_MESSAGE, timeout=5)

