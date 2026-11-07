from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class LoginPage(BasePage):
    USERNAME_INPUT = (By.ID, ":r2:")
    PASSWORD_INPUT=(By.ID, ":r3:")
    SUBMIT_BUTTON=(By.CSS_SELECTOR, "button[type='submit']")
    ERROR_MESSAGE = (By.CSS_SELECTOR, ".MuiBox-root.rtl-1mn67p")

    

    def login(self, username, password):
        self.type(self.USERNAME_INPUT, username)
        self.type(self.PASSWORD_INPUT, password)
        self.click(self.SUBMIT_BUTTON)

    def get_error_message(self):
        return self.get_text(self.ERROR_MESSAGE)


    