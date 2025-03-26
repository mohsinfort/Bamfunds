from playwright.sync_api import Page

class ContactUsPage:
    def __init__(self, page: Page):
        self.page = page
        self.contact_us_link = "//a[normalize-space()='Contact Us']"
        self.email_input = "//input[@type='email']"
        self.submit_button = "//button[@type='submit']"
        self.error_message = "//p[normalize-space()='Invalid e-mail address']"

    def click_contact_us(self):
        """Click the 'Contact Us'."""
        self.page.click(self.contact_us_link)

    def enter_email(self, email):
        """Fills the email field with a given email."""
        self.page.fill(self.email_input, email)

    def click_submit(self):
        """Clicks the Submit button."""
        self.page.click(self.submit_button)

    def get_error_message(self):
        """Returns the text of the error message."""
        return self.page.inner_text(self.error_message)
