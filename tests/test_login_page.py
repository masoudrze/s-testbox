from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from core.config import settings
from pages.login_page import LoginPage


def test_user_can_login(driver, base_url):
    login_page = LoginPage(driver)
    driver.get(base_url)

    login_page.login("student", "Password123")

    WebDriverWait(driver, settings.default_timeout).until(
        EC.url_contains("/logged-in-successfully")
    )


def test_user_cannot_login_with_invalid_credentials(driver, base_url):
    login_page = LoginPage(driver)
    driver.get(base_url)

    login_page.login("invalid_username", "Password123")

    assert login_page.get_error_message() == "Your username is invalid!"
    assert "/practice-test-login" in driver.current_url