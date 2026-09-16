import time

from playwright.sync_api import sync_playwright

def test_open_ecommerce_application(page,base_url):
    # with sync_playwright() as playwright:
        
    #     # Browser
    #     browser = playwright.chromium.launch(headless=False)  
        
    #     #Context
    #     context = browser.new_context()
        
    #     # Page
    #     page = context.new_page()
        
        # Open Application
        page.goto(base_url)
        
        # Keep browser open for 10 seconds
         
            
           