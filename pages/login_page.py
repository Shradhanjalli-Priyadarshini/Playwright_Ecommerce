from pages.base_page import BasePage

class LoginPage (BasePage): # Login inherits functionality from BasePage
    def __init__(self,page):
        
        super().__init__(page) # calls BasePage __init__ page
        
        self.username_input=page.get_by_placeholder("Username")
        self.password_input=page.get_by_placeholder("Password")
        self.login_button = page.get_by_role("button", name="Login")
        
    def open(self, base_url):
            # self.page.goto("https://www.saucedemo.com/")
            self.navigate(base_url) # URL is no longer hardcoded in the page object
            
    def login(self,username,password):
            self.username_input.fill(username)
            self.password_input.fill(password)
            self.login_button.click()