"""
Configurações globais para os testes do Orange HRM
"""
import os
from dataclasses import dataclass


@dataclass
class TestConfig:
    """Configurações de teste"""
    
    # URL do sistema Orange HRM
    BASE_URL: str = "https://opensource-demo.orangehrmlive.com"
    
    # Credenciais de teste (demo)
    USERNAME: str = "Admin"
    PASSWORD: str = "admin123"
    
    # Timeouts
    IMPLICIT_WAIT: int = 10
    EXPLICIT_WAIT: int = 20
    PAGE_LOAD_TIMEOUT: int = 30
    
    # Configurações do navegador
    BROWSER: str = os.getenv("BROWSER", "chrome")
    HEADLESS: bool = os.getenv("HEADLESS", "False").lower() == "true"
    
    # Diretórios
    SCREENSHOTS_DIR: str = "screenshots"
    REPORTS_DIR: str = "reports"
    
    # Dados de teste para Job Vacancy
    TEST_VACANCY_DATA = {
        "vacancy_name": "Senior Software Engineer",
        "job_title": "Software Engineer",
        "description": "We are looking for an experienced software engineer",
        "hiring_manager": "Peter Mac Anderson",
        "number_of_positions": "5"
    }


config = TestConfig()

