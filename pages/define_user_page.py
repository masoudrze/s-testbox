from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class DefineUserPage(BasePage):
    FIRST_NAME_INPUT = (By.CSS_SELECTOR,"input[name='first_name']")
    LAST_NAME_INPUT = (By.CSS_SELECTOR,"input[name='last_name']")
    NATIONAL_NAME_INPUT = (By.CSS_SELECTOR,"input[name='national_code']")
    MOBILE_INPUT = (By.CSS_SELECTOR,"input[name='mobile']")
    USER_NAME_INPUT = (By.CSS_SELECTOR,"input[name='user_name']")
    PASSWORD_INPUT = (By.CSS_SELECTOR,"input[name='password']")
    FIRST_NAME_INPUT = (By.CSS_SELECTOR,"input[name='first_name']")

    USERNAME_INPUT = (By.CSS_SELECTOR, "input[name='username']")
    PASSWORD_INPUT=(By.CSS_SELECTOR, "input[name='password']")
    SUBMIT_BUTTON=(By.CSS_SELECTOR, "button[type='submit']")
    FORGOT_PASSWORD_LINK = (By.CSS_SELECTOR,"a[href='/auth/forget-password']")

    ERROR_MESSAGE = (By.CSS_SELECTOR,"div[role='alert']")


    def login(self, username, password):
        self.type(self.USERNAME_INPUT, username)
        self.type(self.PASSWORD_INPUT, password)
        self.click(self.SUBMIT_BUTTON)

    def foget_password(self):
        self.click(self.FORGOT_PASSWORD_LINK)

    def get_error_message(self):
        return self.get_text(self.ERROR_MESSAGE)




    