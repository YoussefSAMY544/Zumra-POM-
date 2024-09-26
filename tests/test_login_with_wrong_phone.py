import time

import pytest

from pages.home_page import HomePage
from pages.login_page import LoginPage


class TestLoginWithWrongPhone:

    def test_login_with_wrong_phone(self, setup):
        driver = setup
        driver.get("https://zumrafood.com/en")

        # Simulating the login steps
        home_page = HomePage(driver)
        login_page = LoginPage(driver)

        # Navigate to login page
        home_page.navigate_to_login_page()
        time.sleep(10)
        # Enter invalid phone number
        login_page.enter_phone_number("867676767876")
        time.sleep(10)
        # Try to continue
        login_page.click_continue()

        # Assert that the error message appears
        assert login_page.get_error_message() == "Mobile is required!"
