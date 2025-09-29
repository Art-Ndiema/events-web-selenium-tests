import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from utils.driver_manager import DriverManager
from pages.login_page import LoginPage
from pages.events_page import EventsPage
import time

def test_create_event_complete():
    """Test creating event with ALL required fields"""
    print("\n🧪 TEST: Create Complete Event")
    driver = DriverManager.get_driver()
    login_page = LoginPage(driver)
    events_page = EventsPage(driver)
    
    try:
        # Login
        login_page.navigate()
        time.sleep(3)
        login_page.login_with_valid_credentials()
        time.sleep(5)
        
        # Create event
        events_page.click_create_event()
        print("✅ Opened create event form")
        
        # Fill ALL required fields
        event_name = "AutoTest " + str(int(time.time()))
        events_page.create_complete_event(
            event_name=event_name,
            expected_audience="5000",
            start_date="10/01/2025",
            start_time="14:00",
            end_date="10/01/2025",
            end_time="20:00"
        )
        print("✅ Filled all required fields")
        
        # Submit
        events_page.submit_event()
        print("✅ Submitted event")
        
        # Handle success modal
        if events_page.close_success_modal():
            print("✅ Success notification appeared")
        
        # Verify Event Details page
        time.sleep(3)
        if events_page.is_on_event_details_page():
            print("✅ TEST PASSED: On Event Details page")
            return True
        else:
            print("❌ TEST FAILED")
            return False
            
    finally:
        time.sleep(5)
        driver.quit()

if __name__ == "__main__":
    test_create_event_complete()