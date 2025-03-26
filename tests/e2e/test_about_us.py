import pytest
from utils import config
from pages.about_us_page import AboutUsPage

def test_about_us_navigation_and_founders(page):
    about_us = AboutUsPage(page)
    about_us.page.goto(config.BASE_URL)  # Replace with your actual website

    # Hover over "About Us" and click "Leadership"
    about_us.hover_over_about_us()
    about_us.click_leadership()

    # Get and verify founder names
    founders = about_us.get_founders()
    print("Page loaded successfully!", founders)

    assert founders, f"Expected founders, but not found"
