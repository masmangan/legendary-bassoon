import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from pathlib import Path

# Variável global para a URL
ADMIN_URL = "https://opensource-demo.orangehrmlive.com/web/index.php/admin/viewOrganizationGeneralInformation"


def pytest_addoption(parser):
    parser.addoption(
        "--headless", action="store_true", default=False, help="Run tests in headless mode"
    )


@pytest.fixture(scope="session")
def driver(request):
    """
    Fixture principal que inicializa o WebDriver.
    A scope 'session' garante que o navegador seja aberto e fechado apenas uma vez
    para toda a sessão de testes.
    """
    headless = request.config.getoption("--headless")
    options = webdriver.FirefoxOptions()
    if headless:
        options.add_argument("--headless")

    print("Inicializando o navegador...")
    driver = webdriver.Firefox(options=options)
    driver.implicitly_wait(5)  # Espera implícita para estabilidade geral

    yield driver

    # --- Teardown: Fechar o navegador ---
    print("\nFechando o navegador...")
    driver.quit()


@pytest.fixture(scope="module")
def logged_in_driver(driver):
    """
    Fixture com scope 'module' para fazer o login uma única vez por arquivo de teste.
    """
    wait = WebDriverWait(driver, 10)

    # 1. Login
    print("Acessando página de login...")
    driver.get("https://opensource-demo.orangehrmlive.com/")

    wait.until(EC.visibility_of_element_located((By.NAME, "username"))).send_keys("Admin")
    driver.find_element(By.NAME, "password").send_keys("admin123")
    driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

    wait.until(EC.visibility_of_element_located((By.ID, "app")))
    print("Login realizado com sucesso.")

    # 2. Navegar para a página de teste
    driver.get(ADMIN_URL)
    print(f"Navegando para: {ADMIN_URL}")

    org_name_locator = (By.XPATH, "//label[text()='Organization Name']/parent::div/following-sibling::div/input")
    try:
        wait.until(
            lambda d: d.find_element(*org_name_locator).get_attribute("value") != ""
        )
        print("Página de organização carregada e campo 'Organization Name' preenchido.")
    except TimeoutException:
        print("Alerta: O campo 'Organization Name' não foi preenchido após a espera.")

    yield driver

    # --- Teardown: Logout no final do módulo ---
    print("\nRealizando logout...")
    try:
        logout_wait = WebDriverWait(driver, 10)
        user_dropdown = logout_wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".oxd-userdropdown-tab")))
        user_dropdown.click()

        logout_link = logout_wait.until(EC.element_to_be_clickable((By.XPATH, "//a[text()='Logout']")))
        logout_link.click()

        logout_wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".orangehrm-login-title")))
        print("Logout realizado com sucesso.")
    except Exception as e:
        print(f"Erro durante o logout: {e}")


# Criação antecipada das pastas de relatório
def pytest_configure(config):
    from pathlib import Path
    base_dir = Path(__file__).resolve().parents[1]  # .../orange_tests
    reports_dir = base_dir / "reports"
    (reports_dir / "html").mkdir(parents=True, exist_ok=True)
    (reports_dir / "xml").mkdir(parents=True, exist_ok=True)
    (reports_dir / "logs").mkdir(parents=True, exist_ok=True)
    (reports_dir / "screenshots").mkdir(parents=True, exist_ok=True)
    screenshots_dir = reports_dir / "screenshots"
    reports_dir.mkdir(parents=True, exist_ok=True)
    screenshots_dir.mkdir(parents=True, exist_ok=True)

# Captura de screenshot em caso de falha
import pytest

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()
    if report.when == "call":
        driver = None
        if "logged_in_driver" in item.fixturenames:
            driver = item.funcargs.get("logged_in_driver")
        elif "driver" in item.fixturenames:
            driver = item.funcargs.get("driver")
        if driver:
            from pathlib import Path
            screenshots_dir = Path(__file__).resolve().parents[1] / "reports" / "screenshots"
            screenshots_dir.mkdir(parents=True, exist_ok=True)
            status = "passed" if report.passed else "failed"
            filename = item.nodeid.replace("::", "__").replace("/", "_").replace("\\", "_") + f"__{status}.png"
            driver.save_screenshot(str(screenshots_dir / filename))