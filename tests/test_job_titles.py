import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

from pages.login_page import LoginPage
from pages.admin_job_titles_page import JobTitlesPage

@pytest.fixture
def driver():
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    driver.get("https://opensource-demo.orangehrmlive.com/")
    driver.maximize_window()
    yield driver
    driver.quit()

def test_create_job_title(driver):
    login = LoginPage(driver)
    login.login("Admin", "admin123")

    job_page = JobTitlesPage(driver)
    job_page.open_job_titles()
    job_page.create_job_title("QA Automation Tester")
    job_page.search_job_title("QA Automation Tester")

    assert job_page.job_title_exists("QA Automation Tester") is True
