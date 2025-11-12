"""
Configurações e fixtures do pytest para os testes
"""
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
import os
from datetime import datetime
from .config import config as test_config


@pytest.fixture(scope="function")
def driver():
    """
    Fixture que inicializa o WebDriver e finaliza após o teste
    """
    driver = None
    
    try:
        if test_config.BROWSER.lower() == "chrome":
            options = ChromeOptions()
            if test_config.HEADLESS:
                options.add_argument("--headless=new")
            options.add_argument("--no-sandbox")
            options.add_argument("--disable-dev-shm-usage")
            options.add_argument("--disable-gpu")
            options.add_argument("--window-size=1920,1080")
            options.add_argument("--disable-blink-features=AutomationControlled")
            options.add_experimental_option("excludeSwitches", ["enable-logging"])
            
            # Usar ChromeDriverManager com cache
            try:
                driver_path = ChromeDriverManager().install()
                
                # Fix: webdriver-manager às vezes retorna caminho errado no Windows
                # Se o caminho não termina com .exe, procurar o executável correto
                if not driver_path.endswith('.exe'):
                    import os
                    import glob
                    
                    # Obter o diretório base
                    base_dir = os.path.dirname(driver_path)
                    
                    # Procurar por chromedriver.exe no diretório
                    pattern = os.path.join(base_dir, '*chromedriver.exe')
                    matches = glob.glob(pattern)
                    
                    if matches:
                        driver_path = matches[0]
                        print(f"ChromeDriver encontrado em: {driver_path}")
                    else:
                        # Procurar em subdiretórios
                        pattern = os.path.join(base_dir, '**', '*chromedriver.exe')
                        matches = glob.glob(pattern, recursive=True)
                        if matches:
                            driver_path = matches[0]
                            print(f"ChromeDriver encontrado em: {driver_path}")
                
                service = ChromeService(executable_path=driver_path)
                driver = webdriver.Chrome(service=service, options=options)
            except Exception as e:
                print(f"Erro ao instalar ChromeDriver via manager: {e}")
                # Tentar sem especificar service (usar driver do PATH)
                try:
                    driver = webdriver.Chrome(options=options)
                except Exception as e2:
                    print(f"Erro ao usar Chrome do PATH: {e2}")
                    raise Exception(
                        "Não foi possível inicializar o ChromeDriver. "
                        "Por favor, execute: python test_driver_setup.py para diagnóstico, "
                        "ou consulte TROUBLESHOOTING.md"
                    )
            
        elif test_config.BROWSER.lower() == "firefox":
            options = FirefoxOptions()
            if test_config.HEADLESS:
                options.add_argument("--headless")
            
            try:
                driver_path = GeckoDriverManager().install()
                service = FirefoxService(executable_path=driver_path)
                driver = webdriver.Firefox(service=service, options=options)
            except Exception as e:
                print(f"Erro ao instalar GeckoDriver via manager: {e}")
                driver = webdriver.Firefox(options=options)
        
        # Configurar timeouts
        driver.implicitly_wait(test_config.IMPLICIT_WAIT)
        driver.set_page_load_timeout(test_config.PAGE_LOAD_TIMEOUT)
        driver.maximize_window()
        
        yield driver
        
    finally:
        if driver:
            try:
                driver.quit()
            except Exception:
                pass


@pytest.fixture(scope="function")
def authenticated_driver(driver):
    """
    Fixture que retorna um driver já autenticado no sistema
    """
    from .pages.login_page import LoginPage
    
    login_page = LoginPage(driver)
    login_page.open()
    login_page.login(test_config.USERNAME, test_config.PASSWORD)
    
    yield driver


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """
    Hook para capturar screenshots em caso de falha
    """
    outcome = yield
    report = outcome.get_result()
    
    if report.when == "call" and report.failed:
        driver = item.funcargs.get('driver') or item.funcargs.get('authenticated_driver')
        if driver:
            # Criar diretório de screenshots se não existir
            os.makedirs(test_config.SCREENSHOTS_DIR, exist_ok=True)
            
            # Nome do arquivo com timestamp
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            screenshot_name = f"{item.name}_{timestamp}.png"
            screenshot_path = os.path.join(test_config.SCREENSHOTS_DIR, screenshot_name)
            
            # Capturar screenshot
            driver.save_screenshot(screenshot_path)
            print(f"\nScreenshot salvo: {screenshot_path}")


def pytest_configure(config):
    """
    Configuração inicial do pytest
    """
    # Criar diretórios necessários
    os.makedirs(test_config.SCREENSHOTS_DIR, exist_ok=True)
    os.makedirs(test_config.REPORTS_DIR, exist_ok=True)

