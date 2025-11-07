from .base_page import BasePage

class Sidebar(BasePage):
    def open_leave_apply(self):
        self.x("//span[text()='Leave']").click()
        self.x("//a[contains(@href,'viewApplyLeave')]").click()

    def open_my_leave(self):
        self.x("//span[text()='Leave']").click()
        self.x("//a[contains(@href,'viewMyLeaveList')]").click()

    def open_leave_list(self):
        self.x("//span[text()='Leave']").click()
        self.x("//a[contains(@href,'viewLeaveList')]").click()
