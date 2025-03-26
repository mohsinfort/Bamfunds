import pytest
from utils import config
from pages.contact_us_page import ContactUsPage

def test_contact_us_navigation_and_errors(page):
    contact_us = ContactUsPage(page)
    contact_us.page.goto(config.BASE_URL)

    contact_us.click_contact_us()

    contact_us.enter_email("invalid-email@test.com")
    contact_us.click_submit()
    contact_us.enter_email("invalid-email")

    # Verify error message
    expected_error = "Invalid e-mail address"
    actual_error = contact_us.get_error_message()
    
    assert expected_error in actual_error, f"Expected '{expected_error}', but got '{actual_error}'"
