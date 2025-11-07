from .base_page import BasePage

class LoginPage(BasePage):
    def open(self, base_url):
        self.driver.get(base_url)

    def login(self, user, pwd):
        self.css("input[name='username']").send_keys(user)
        self.css("input[name='password']").send_keys(pwd)
        self.css("button[type='submit']").click()
