from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from config.config import Config

class LoginPage(BasePage):
    # Locators
    USERNAME_FIELD = (By.XPATH, "//input[@placeholder='Enter username']")
    PASSWORD_FIELD = (By.NAME, "password")
    LOGIN_BUTTON = (By.XPATH, "//button[contains(text(), 'Login')]")
    
    def navigate(self):
        self.driver.get(Config.LOGIN_URL)
    
    def login(self, username, password):
        self.enter_text(self.USERNAME_FIELD, username)
        self.enter_text(self.PASSWORD_FIELD, password)
        self.click(self.LOGIN_BUTTON)
    
    def login_with_valid_credentials(self):
        self.login(Config.VALID_USERNAME, Config.VALID_PASSWORD)