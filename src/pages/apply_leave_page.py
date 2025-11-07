from .base_page import BasePage

class ApplyLeavePage(BasePage):
    def select_type(self, type_label="Annual Leave"):
        self.css("div.oxd-select-text-input").click()
        self.x(f"//span[normalize-space(text())='{type_label}']").click()

    def set_from_date(self, yyyy_mm_dd):
        inputs = self.driver.find_elements("css selector", "input[placeholder='yyyy-mm-dd']")
        inputs[0].clear()
        inputs[0].send_keys(yyyy_mm_dd)

    def set_comment(self, text):
        self.driver.find_element("tag name","textarea").send_keys(text)

    def submit(self):
        self.css("button[type='submit']").click()
