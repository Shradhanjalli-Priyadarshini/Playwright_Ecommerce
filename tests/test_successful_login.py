from playwright.sync_api import sync_playwright, expect
from pages.login_page import LoginPage
from data.users import STANDARD_USER
import time
import pytest

@pytest.mark.smoke
@pytest.mark.login
def test_successful_login(page, base_url):
    
    login_page = LoginPage(page)
    
    login_page.open(base_url)

    login_page.login(
        username=STANDARD_USER["username"],
        password=STANDARD_USER["password"]
    )

    expect(
        page.get_by_text("Products")
    ).to_be_visible()
    
    # page.goto("https://www.saucedemo.com/")
    
    # page.get_by_placeholder("Username").fill("standard_user")
    # page.get_by_placeholder("Password").fill("secret_sauce")
    # page.get_by_role("button", name = "Login").click()
    
    # expect(page.get_by_text("Products")).to_be_visible()
