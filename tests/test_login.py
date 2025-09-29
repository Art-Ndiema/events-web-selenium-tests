import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from utils.driver_manager import DriverManager
from pages.login_page import LoginPage
from config.config import Config
import time

def test_valid_login():
    driver = DriverManager.get_driver()
    login_page = LoginPage(driver)
    
    try:
        login_page.navigate()
        time.sleep(3)
        login_page.login_with_valid_credentials()
        time.sleep(5)
        
        assert "login" not in login_page.get_current_url()
        print("✅ Valid login test PASSED")
    finally:
        driver.quit()

def test_invalid_login():
    driver = DriverManager.get_driver()
    login_page = LoginPage(driver)
    
    try:
        login_page.navigate()
        time.sleep(3)
        login_page.login(Config.INVALID_USERNAME, Config.INVALID_PASSWORD)
        time.sleep(5)
        
        assert "login" in login_page.get_current_url()
        print("✅ Invalid login test PASSED")
    finally:
        driver.quit()

if __name__ == "__main__":
    test_valid_login()
    test_invalid_login()