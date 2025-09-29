"""
Configuration file for test automation framework
Contains URLs, credentials, timeouts, and browser settings
"""

class Config:
    # Base URLs
    BASE_URL = "https://events-uat.pagamio.tech"
    LOGIN_URL = f"{BASE_URL}/login?callbackUrl=%2Fevents%2Fsearch"
    EVENTS_SEARCH_URL = f"{BASE_URL}/events/search"
    
    # Valid Test Credentials
    VALID_USERNAME = "TestGrace"
    VALID_PASSWORD = "pagamio123"
    
    # Invalid Test Credentials
    INVALID_USERNAME = "InvalidUser"
    INVALID_PASSWORD = "wrongpassword123"
    
    # Browser Settings
    BROWSER = "chrome"  # can be changed to "firefox", "edge", etc.
    HEADLESS = False  # Set to True to run without opening browser
    
    # Timeouts (in seconds)
    IMPLICIT_WAIT = 10
    PAGE_LOAD_TIMEOUT = 30
    SHORT_WAIT = 3
    MEDIUM_WAIT = 5
    LONG_WAIT = 10
    
    # Browser Options
    CHROME_OPTIONS = [
        "--no-sandbox",
        "--disable-dev-shm-usage",
        "--start-maximized"
    ]