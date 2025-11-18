"""
Teste de Sistema (E2E) - Criar Vaga de Trabalho
Orange HRM - Verificação e Validação de Software
"""
import time
from .pages.login_page import LoginPage
from .pages.recruitment_page import RecruitmentPage
from .config import config


class TestCreateJobVacancy:
    """Teste end-to-end para criação de vagas de trabalho"""
    
    def test_create_vacancy_complete_flow(self, driver):
        """
        Fluxo completo: Login → Navegação → Criação → Salvamento
        
        Cenário:
        1. Usuário faz login no sistema
        2. Navega para Recruitment > Vacancies
        3. Clica em Add para criar nova vaga
        4. Preenche os campos obrigatórios do formulário
        5. Salva a vaga
        """
        print("\n=== TESTE: Criar Vaga de Trabalho ===\n")
        
        # 1. Login no sistema
        print("1. Fazendo login...")
        login_page = LoginPage(driver)
        login_page.open()
        login_page.login(config.USERNAME, config.PASSWORD)
        assert login_page.is_login_successful(), "Falha no login"
        print("   ✓ Login OK\n")
        
        # 2. Navegar para Vacancies
        print("2. Navegando para Recruitment > Vacancies...")
        recruitment_page = RecruitmentPage(driver)
        recruitment_page.navigate_to_vacancies()
        print("   ✓ Navegação OK\n")
        
        # 3. Clicar em Add
        print("3. Clicando em Add...")
        recruitment_page.click_add_vacancy()
        time.sleep(1)
        print("   ✓ Formulário aberto\n")
        
        # 4. Preencher formulário PASSO A PASSO
        vacancy_name = 'Senior Software Engineer - E2E Test'
        
        print("4. Preenchendo formulário...")
        print("   - Vacancy Name...")
        recruitment_page.fill_vacancy_name(vacancy_name)
        time.sleep(0.5)
        
        print("   - Job Title...")
        recruitment_page.select_job_title('Software Engineer')
        time.sleep(1)
        
        print("   - Description...")
        recruitment_page.fill_description('Looking for an experienced engineer with Python and Selenium expertise')
        time.sleep(0.5)
        
        print("   - Hiring Manager...")
        recruitment_page.select_hiring_manager('Peter Mac Anderson')
        time.sleep(2)  # Aguardar autocomplete
        
        print("   - Number of Positions...")
        recruitment_page.fill_number_of_positions('3')
        time.sleep(0.5)
        print("   ✓ Formulário preenchido\n")
        
        # 5. Salvar
        print("5. Salvando vaga...")
        recruitment_page.click_save()
        print("   ✓ Botão Save clicado\n")
        
        print("=== TESTE CONCLUÍDO ===\n")
        print("Aguardando 5 segundos para visualização...")
        time.sleep(5)
