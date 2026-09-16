from playwright.sync_api import sync_playwright, expect
import time
from conftest import base_url
from pages.login_page import LoginPage
from data.users import STANDARD_USER

def test_login(page, base_url):
    # with sync_playwright() as playwright:
    #     browser = playwright.chromium.launch(headless=False)
        
    #     context = browser.new_context()
    #     page = context.new_page()
        
        # page.goto("https://www.saucedemo.com/")
        
        # page.get_by_placeholder("Username").fill("standard_user")
        # page.get_by_placeholder("Password").fill("secret_sauce")
        # page.get_by_role("button", name="Login").click()
        
        login_page = LoginPage(page)
        login_page.open(base_url)
            
        login_page.login(
                username=STANDARD_USER["username"],
                password=STANDARD_USER["password"]
            )
        
        # Assertion:1 URL
        expect(page).to_have_url("https://www.saucedemo.com/inventory.html")
        
        # Assertion 2: Products title
        expect(page.get_by_text("Products")).to_be_visible()
        
        # Assertion 3: Products count
        expect(page.locator(".inventory_item")).to_have_count(6)       
        
        # verify products page
        print(page.get_by_text("Products").is_visible())
        
      