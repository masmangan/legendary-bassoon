import os, time
from selenium.webdriver.common.by import By

def shoot(driver, name):
    path = os.path.join("docs","screenshots", f"{int(time.time())}_{name}.png")
    driver.save_screenshot(path)
    return path

def by_text(driver, tag, text):
    # Busca por texto visível (robusto quando CSS muda)
    return driver.find_element(By.XPATH, f"//{tag}[normalize-space(text())='{text}']")
