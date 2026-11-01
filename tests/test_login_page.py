from pages.login_page import LoginPage


def test_user_can_login(driver, base_url):
        login_page = LoginPage(driver)

        driver.get(f"{base_url}")
        login_page.login("student", "student123")

        assert "/logged-in-successfully" in driver.current_url





def test_user_cannot_login_with_invalid_credentials(driver, base_url):
        login_page = LoginPage(driver)

        driver.get(f"{base_url}")
        login_page.login("invalid_username", "invalid_password")

        assert "/practice-test-login" in driver.current_url
        assert login_page.get_error_message() == "Invalid username or password"