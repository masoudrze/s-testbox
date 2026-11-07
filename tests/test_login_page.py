from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from core.config import settings
from pages.login_page import LoginPage


def test_user_can_login(driver, base_url):
    login_page = LoginPage(driver)
    driver.get(base_url)

    login_page.login("masoud", "123456")

    otp = input("Enter 6-digit otp:").strip()
    login_page.enter_otp(otp)

    WebDriverWait(driver, settings.default_timeout).until(
        EC.url_contains("/admin/dashboard")
    )


def test_user_cannot_login_with_invalid_credentials(driver, base_url):
    login_page = LoginPage(driver)
    driver.get(base_url)

    login_page.login("test", "test123456")

    assert login_page.get_error_message() == "Your username is invalid!"
    assert "/practice-test-login" in driver.current_url