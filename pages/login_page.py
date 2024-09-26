from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 20)  # 20-second wait for elements

    phone_input_field = (By.XPATH,'//*[@placeholder="Phone Number"]')
    continue_button = (By.XPATH, "/html/body/div/div/div/div/div/main/div/div/div[2]/form/button/span")
    error_message = (By.CLASS_NAME, "v-messages__message")
    login_button = (By.CSS_SELECTOR, "#header > div > div > div > div.user-section > a:nth-child(3) > span > span.header-action-text")

    def navigate_to_login_page(self):
        self.navigate_to_home_page()
        login_button_element = self.wait.until(EC.element_to_be_clickable(self.login_button))
        login_button_element.click()
        assert self.driver.current_url == "https://zumrafood.com/en/login", "Did not navigate to login page."

    def enter_phone_number(self, phone_number):
        phone_input = self.wait.until(EC.presence_of_element_located(self.phone_input_field))
        phone_input.click()  # Click the phone input field
        phone_input.send_keys(phone_number)  # Enter the phone number

    def click_continue(self):
        continue_btn = self.wait.until(EC.element_to_be_clickable(self.continue_button))
        continue_btn.click()

    def get_error_message(self):
        error_msg = self.wait.until(EC.visibility_of_element_located(self.error_message))
        return error_msg.text
