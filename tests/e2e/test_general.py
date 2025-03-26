import re
from utils import config
from playwright.sync_api import Page, expect

def test_has_title(page: Page):
    page.goto(config.BASE_URL)

    # Expect a title "to contain" a substring.
    expect(page).to_have_title(re.compile("Balyasny Asset Management"))