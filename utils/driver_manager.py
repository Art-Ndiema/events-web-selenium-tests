from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from config.config import Config

class DriverManager:
    @staticmethod
    def get_driver():
        chrome_options = Options()
        for option in Config.CHROME_OPTIONS:
            chrome_options.add_argument(option)
        
        service = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service, options=chrome_options)
        driver.implicitly_wait(Config.IMPLICIT_WAIT)
        return driver