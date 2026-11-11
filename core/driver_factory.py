from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.remote.webdriver import WebDriver

from pathlib import Path
from selenium.common.exceptions import NoSuchDriverException
from selenium.webdriver.chrome.service import Service

from core.config import settings


def create_driver() -> WebDriver:
    if settings.browser == "chrome":
        return create_chrome_driver()

    if settings.browser == "firefox":
        return create_firefox_driver()

    raise ValueError(f"Unsupported browser: {settings.browser}")



def create_chrome_driver() -> WebDriver:
    options = ChromeOptions()

    if settings.headless:
        options.add_argument("--headless=new")

    options.add_argument("--window-size=1920,1080")
    options.add_argument("--disable-notifications")

    # try:
    #     return webdriver.Chrome(options=options)

    # except NoSuchDriverException as error:
    driver_path = (
            Path(__file__).resolve().parent.parent
            / "drivers"
            / "chromedriver.exe"
        )

        # if not driver_path.is_file():
        #     raise FileNotFoundError(
        #         f"Local ChromeDriver not found: {driver_path}"
        #     ) from error

    return webdriver.Chrome(
            service=Service(executable_path=str(driver_path)),
            options=options,
        )

def create_firefox_driver() -> WebDriver:
    options = FirefoxOptions()

    if settings.headless:
        options.add_argument("-headless")

    driver = webdriver.Firefox(options=options)
    driver.set_window_size(1920, 1080)

    return driver
