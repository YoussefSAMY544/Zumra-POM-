from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class HomePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)  # 10-second wait for elements

    # Locator for the login button
    login_button = (By.CSS_SELECTOR, "#header > div > div > div > div.user-section > a:nth-child(3) > span > span.header-action-text")

    # Navigate to home page
    def navigate_to_home_page(self):
        self.driver.get("https://zumrafood.com/en")

    # Click on the login button to navigate to the login page
    def navigate_to_login_page(self):
        # First navigate to the home page
        self.navigate_to_home_page()

        # Wait for the login button to be clickable and then click it
        login_button_element = self.wait.until(EC.element_to_be_clickable(self.login_button))
        login_button_element.click()

        # Optional: Verify that the current URL is the login page
        assert self.driver.current_url == "https://zumrafood.com/en/login", "Failed to navigate to login page."
