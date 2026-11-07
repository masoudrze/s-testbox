from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class LoginPage(BasePage):
    USERNAME_INPUT = (By.ID, ":r2:")
    PASSWORD_INPUT=(By.ID, ":r3:")
    SUBMIT_BUTTON=(By.CSS_SELECTOR, "button[type='submit']")
    ERROR_MESSAGE = (By.CSS_SELECTOR, ".MuiBox-root.rtl-1mn67p")

    OPT_IDS = [":r8:",":r9:",":ra:",":rb:",":rc:",":rd:"]

    def login(self, username, password):
        self.type(self.USERNAME_INPUT, username)
        self.type(self.PASSWORD_INPUT, password)
        self.click(self.SUBMIT_BUTTON)

    def get_error_message(self):
        return self.get_text(self.ERROR_MESSAGE)

    def enter_otp(self, otp):
        assert len(otp) == 6 and otp.isascii() and otp.isdigit()
        
        for otp_id, digit in zip(self.OPT_IDS, otp):
            self.type((By.ID, otp_id),digit)


    