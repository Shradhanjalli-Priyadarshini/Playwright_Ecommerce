from playwright.sync_api import sync_playwright
import time

def test_login_locators(page): # pytest gives test a ready-ro-use playwright page
    
        
        page.goto("https://www.saucedemo.com/")
        page.locator("#user-name").fill("standard_user")
        
        page.locator("#password").fill("secret_sauce")
        
        page.locator("#login-button").click()
        
        assert page.url == "https://www.saucedemo.com/inventory.html"
            
        
