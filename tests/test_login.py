from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time

def test_login():
    """Test user login functionality"""
    print("Starting login test...")

    # Set up Chrome options
    chrome_options = Options()
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")

    # Use webdriver-manager for automatic ChromeDriver management
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=chrome_options)

    try:
        # Navigate to login page
        driver.get("https://events-uat.pagamio.tech/login?callbackUrl=%2Fevents%2Fsearch")
        print("Successfully opened login page!")
        
        # Wait for page to load
        time.sleep(5)
        
        # Find and fill username field
        username_field = driver.find_element(By.XPATH, "//input[@placeholder='Enter username']")
        username_field.send_keys("TestGrace")
        print("✅ Entered username: TestGrace")
        
        # Find and fill password field
        password_field = driver.find_element(By.NAME, "password")
        password_field.send_keys("pagamio123")
        print("✅ Entered password")
        
        # Find and click login button
        login_button = driver.find_element(By.XPATH, "//button[contains(text(), 'Login')]")
        login_button.click()
        print("✅ Clicked login button")
        
        # Wait for login to process and page to redirect
        time.sleep(8)
        
        # Check if login was successful by looking at the URL
        current_url = driver.current_url
        print(f"Current URL after login: {current_url}")
        
        # Check if we're no longer on the login page
        if "login" not in current_url:
            print("✅ Login appears successful - redirected away from login page!")
        else:
            print("❌ Still on login page - login may have failed")
        
        # Get the page title after login
        title = driver.title
        print(f"Page title after login: {title}")
        
    finally:
        # Keep browser open for 5 seconds so you can see the result
        time.sleep(5)
        driver.quit()
        print("Browser closed successfully!")

if __name__ == "__main__":
    test_login()