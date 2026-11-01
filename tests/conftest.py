from collections.abc import Iterator

import pytest
from selenium.webdriver.remote.webdriver import WebDriver

from core.config import settings
from core.driver_factory import create_driver


@pytest.fixture(scope="session")
def base_url() -> str:
    return settings.base_url


@pytest.fixture
def driver() -> Iterator[WebDriver]:
    web_driver = create_driver()

    try:
        yield web_driver
    finally:
        web_driver.quit()