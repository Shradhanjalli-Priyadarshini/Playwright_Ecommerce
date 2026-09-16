class BasePage:
    def __init__(self, page):
        self.page = page
        
# It gives us a reusable parent class

    def navigate(self,url):
        self.page.goto(url)

    def get_current_url(self): # now every page objects inherits this method
        return self.page.url 
    
    def take_screenshot(self, file_name):
        self.page.screenshot(path=file_name)
        