import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from pages.base_page import BasePage
from config.config import Config
import time

class EventsPage(BasePage):
    # Locators
    CREATE_EVENT_BUTTON = (By.XPATH, "//button[contains(text(), 'Create Event')]")
    EVENT_NAME_FIELD = (By.XPATH, "//label[text()='Event Name']/following-sibling::input")
    EXPECTED_AUDIENCE_FIELD = (By.XPATH, "//label[text()='Expected Audience']/following-sibling::input")
    
    # Date/Time - These are date pickers, need special handling
    START_DATE_PICKER = (By.XPATH, "//label[text()='Start Date']/following-sibling::div//input")
    START_TIME_PICKER = (By.XPATH, "//label[text()='Start Time']/following-sibling::div//input")
    END_DATE_PICKER = (By.XPATH, "//label[text()='End Date']/following-sibling::div//input")
    END_TIME_PICKER = (By.XPATH, "//label[text()='End Time']/following-sibling::div//input")
    
    # Buttons
    SUBMIT_BUTTON = (By.XPATH, "//button[text()='Submit']")
    
    # Success modal
    GOT_IT_BUTTON = (By.XPATH, "//button[text()='Got it']")
    
    def navigate(self):
        self.driver.get(Config.EVENTS_SEARCH_URL)
    
    def click_create_event(self):
        self.click(self.CREATE_EVENT_BUTTON)
        time.sleep(2)
    
    def enter_event_name(self, name):
        self.enter_text(self.EVENT_NAME_FIELD, name)
    
    def enter_expected_audience(self, audience):
        """Enter expected audience - ensures it doesn't start with 0"""
        audience_str = str(audience).lstrip('0')  # Remove leading zeros
        if not audience_str:  # If all zeros, make it "1"
            audience_str = "1"
        self.enter_text(self.EXPECTED_AUDIENCE_FIELD, audience_str)
    
    def set_start_date(self, date_string="10/01/2025"):
        """Set start date - format MM/DD/YYYY"""
        field = self.find_element(self.START_DATE_PICKER)
        field.click()
        time.sleep(1)
        field.clear()
        field.send_keys(date_string)
        field.send_keys(Keys.ENTER)
        time.sleep(1)
    
    def set_start_time(self, time_string="12:00"):
        """Set start time - format HH:MM"""
        field = self.find_element(self.START_TIME_PICKER)
        field.click()
        time.sleep(1)
        field.clear()
        field.send_keys(time_string)
        time.sleep(1)
    
    def set_end_date(self, date_string="10/02/2025"):
        """Set end date - format MM/DD/YYYY"""
        field = self.find_element(self.END_DATE_PICKER)
        field.click()
        time.sleep(1)
        field.clear()
        field.send_keys(date_string)
        field.send_keys(Keys.ENTER)
        time.sleep(1)
    
    def set_end_time(self, time_string="18:00"):
        """Set end time - format HH:MM"""
        field = self.find_element(self.END_TIME_PICKER)
        field.click()
        time.sleep(1)
        field.clear()
        field.send_keys(time_string)
        time.sleep(1)
    
    def create_complete_event(self, event_name, expected_audience, 
                             start_date="10/01/2025", start_time="12:00",
                             end_date="10/02/2025", end_time="18:00"):
        """Create event with ALL required fields"""
        self.enter_event_name(event_name)
        self.enter_expected_audience(expected_audience)
        self.set_start_date(start_date)
        self.set_start_time(start_time)
        self.set_end_date(end_date)
        self.set_end_time(end_time)
    
    def submit_event(self):
        self.click(self.SUBMIT_BUTTON)
        time.sleep(3)
    
    def close_success_modal(self):
        try:
            self.click(self.GOT_IT_BUTTON)
            time.sleep(2)
            return True
        except:
            return False
    
    def is_on_event_details_page(self):
        return "Event Details" in self.driver.page_source