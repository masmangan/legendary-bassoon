import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

@pytest.fixture(scope="session")
def base_url():
    return "https://opensource-demo.orangehrmlive.com/"

@pytest.fixture
def driver():
    opts = Options()
    opts.add_argument("--start-maximized")
    service = Service(ChromeDriverManager().install())
    drv = webdriver.Chrome(service=service, options=opts)
    drv.implicitly_wait(6) 
    yield drv
    drv.quit()
