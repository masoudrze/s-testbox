from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from core.config import settings
from pages.login_page import LoginPage

import time



def test_user_cannot_login_with_shortlen_pass(driver, base_url):
    login_page = LoginPage(driver)
    driver.get(base_url)

    login_page.login("test", "test")

    assert login_page.get_error_message() == "password:مطمعن شوید طول این مقدار حداقل 6 است."
    assert "/auth/login" in driver.current_url




def test_user_cannot_login_with_invalid_credentials(driver, base_url):
    login_page = LoginPage(driver)
    driver.get(base_url)

    login_page.login("test", "test123456")

    assert login_page.get_error_message() == "نام کاربری یا کلمه عبور اشتباه می باشد"
    assert "/auth/login" in driver.current_url




def test_user_can_login(driver, base_url):
    login_page = LoginPage(driver)
    driver.get(base_url)

    login_page.login("masoud", "123456")

    #otp = input("Enter 6-digit otp:").strip()
    #login_page.enter_otp(otp)
    time.sleep(15)

    WebDriverWait(driver, settings.default_timeout).until(
        EC.url_contains("/admin/dashboard")
    )


def test_forget_password_navigation(driver, base_url):
    login_page = LoginPage(driver)
    driver.get(base_url)

    login_page.foget_password()

    #assert login_page.get_error_message() == "نام کاربری یا کلمه عبور اشتباه می باشد"
    assert "/auth/forget-password" in driver.current_url