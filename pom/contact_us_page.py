
class ContactUsPage:
    def __init__(self, page):
        self.page = page


    def navigate_contactUs(self):
        self.page.goto("https://symonstorozhenko.wixsite.com/website-1/contact")

    def submitForm(self, name, address, email, phone, subject, message):
        self.page.fill("[placeholder=\"Enter your name\"]", name)
        self.page.fill("[placeholder=\"Enter your address\"]", address)
        self.page.fill("[placeholder=\"Enter your email\"]", email)
        self.page.fill("[placeholder=\"Enter your phone number\"]", phone)
        self.page.fill("[placeholder=\"Type the subject\"]", subject)
        self.page.fill("[placeholder=\"Type your message here...\"]", message)


