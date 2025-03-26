from playwright.sync_api import Page

class AboutUsPage:
    def __init__(self, page: Page):
        self.page = page
        self.about_us_menu = "text=About Us"
        self.leadership_link = "text=Leadership"
        self.founders_section = "//body/div/main/div[2]/div[1]/div[2]/*"

    def hover_over_about_us(self):
        """Hover over the 'About Us' menu."""
        self.page.hover(self.about_us_menu)

    def click_leadership(self):
        """Click the 'Leadership' option after hovering over 'About Us'."""
        self.page.click(self.leadership_link)

    def get_founders(self):
        """Return a list of founder names."""
        return self.page.locator(self.founders_section)
    