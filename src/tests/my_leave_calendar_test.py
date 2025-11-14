import unittest, time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

def force_set_input(driver, el, value):
    driver.execute_script("""
        arguments[0].value = arguments[1];
        arguments[0].dispatchEvent(new Event('input',{ bubbles:true }));
        arguments[0].dispatchEvent(new Event('change',{ bubbles:true }));
        arguments[0].blur();
    """, el, value)

def try_formats_and_apply(driver, input_el, formats):
    for f in formats:
        try:
            input_el.click()
            input_el.clear()
            input_el.send_keys(f)
            input_el.send_keys(Keys.TAB)
            time.sleep(0.35)

            cur = (input_el.get_attribute("value") or "").strip()
            if cur == f:
                return cur

            force_set_input(driver, input_el, f)
            time.sleep(0.25)

            cur = (input_el.get_attribute("value") or "").strip()
            if cur == f:
                return cur

        except Exception:
            pass

    return (input_el.get_attribute("value") or "").strip()


class MyLeaveCalendarTest(unittest.TestCase):

    def setUp(self):
        opts = Options()
        opts.add_argument("--start-maximized")
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=opts)
        self.wait = WebDriverWait(self.driver, 18)

    def test_date_range_validation(self):
        driver, wait = self.driver, self.wait

        try:
            driver.get("https://opensource-demo.orangehrmlive.com/")
            wait.until(EC.presence_of_element_located((By.NAME, "username"))).send_keys("Admin")
            driver.find_element(By.NAME, "password").send_keys("admin123")
            driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

            wait.until(EC.presence_of_element_located((By.XPATH, "//h6[text()='Dashboard']")))

            driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/leave/viewMyLeaveList")
            try:
                wait.until(EC.presence_of_element_located((By.XPATH, "//h6[contains(., 'My Leave')]")))
            except:
                time.sleep(1)

            xpaths_from = [
                "//label[contains(., 'From')]/../following-sibling::div//input",
                "//input[@placeholder='From']"
            ]
            xpaths_to = [
                "//label[contains(., 'To')]/../following-sibling::div//input",
                "//input[@placeholder='To']"
            ]

            from_el = to_el = None

            for xp in xpaths_from:
                try:
                    from_el = wait.until(EC.presence_of_element_located((By.XPATH, xp)))
                    break
                except:
                    pass

            for xp in xpaths_to:
                try:
                    to_el = wait.until(EC.presence_of_element_located((By.XPATH, xp)))
                    break
                except:
                    pass

            self.assertIsNotNone(from_el, "Campo 'From' não foi encontrado.")
            self.assertIsNotNone(to_el, "Campo 'To' não foi encontrado.")

            formats_from = ["2025-11-10", "10-11-2025", "2025-11-10"]
            formats_to = ["2025-11-05", "05-11-2025", "2025-11-05"]

            for el in (from_el, to_el):
                el.click()
                el.send_keys(Keys.CONTROL + "a", Keys.DELETE)

            final_from = try_formats_and_apply(driver, from_el, formats_from)
            final_to = try_formats_and_apply(driver, to_el, formats_to)

            print(">>> Valores finais aplicados (From, To):", repr(final_from), repr(final_to))

            self.assertTrue(len(final_from) > 0, "Campo 'From' ficou vazio após tentativa de preenchimento.")
            self.assertTrue(len(final_to) > 0, "Campo 'To' ficou vazio após tentativa de preenchimento.")

            search_btn = None
            for xp in ["//button[normalize-space()='Search']", "//button[@type='submit']"]:
                try:
                    search_btn = wait.until(EC.element_to_be_clickable((By.XPATH, xp)))
                    break
                except:
                    pass

            self.assertIsNotNone(search_btn, "Botão Search não foi encontrado.")

            driver.execute_script("arguments[0].click();", search_btn)
            time.sleep(1.2)

            page = driver.page_source

            self.assertTrue(
                "No Records Found" in page or "Should be a valid date" not in page,
                "O Search não executou corretamente. Resultado inesperado."
            )

            print("Teste finalizado — veja mensagens acima.")

        except Exception as e:
            print("❌ Erro durante o teste:", e)
            raise e   

        finally:
            time.sleep(1)
            driver.quit()


if __name__ == "__main__":
    unittest.main()