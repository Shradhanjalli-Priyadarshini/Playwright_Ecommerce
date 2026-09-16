import time
import pytest
from playwright.sync_api import sync_playwright,expect
from pages.login_page import LoginPage
from pages.products_page import ProductsPage
from pages.cart_page import CartPage
from data.products import BACKPACK
from data.users import STANDARD_USER

@pytest.mark.regression
@pytest.mark.cart
def test_add_backpacks_to_cart(page, base_url):
    # with sync_playwright() as playwright:
        
        # browser= playwright.chromium.launch(headless=False)
        # context = browser.new_context()
        # page = context.new_page()
        
        # page.goto("https://www.saucedemo.com/")
        
        # page.get_by_placeholder("Username").fill("standard_user")
        # page.get_by_placeholder("Password").fill("secret_sauce")
        # page.get_by_role("button", name="Login").click()
        
        # expect(page).to_have_url("https://www.saucedemo.com/inventory.html")
        
        # expect(page.get_by_text("Products")).to_be_visible()
        
        # # Find backpack
        # backpack = page.locator(".inventory_item").filter(has_text="Sauce Labs Backpack")
        
        # # Add backpack to cart
        # backpack.get_by_role("button", name="Add to cart").click()
      
        # # Verify cart badge
        # cart_badge = page.locator(".shopping_cart_badge")
        
        # expect(cart_badge).to_have_text("1")

        # # Open cart
        # page.locator(".shopping_cart_link").click()
        
        # # Verify backpack in cart
        # expect(page.get_by_text("Sauce Labs Backpack")).to_be_visible()

        # Login Page
        login_page = LoginPage(page)
        
        login_page.open(base_url)
        
        login_page.login(STANDARD_USER["username"],STANDARD_USER["password"])
        
        # Products Page
        products_page = ProductsPage(page)
        
        products_page.add_product_to_cart("Backpack")
        
        # Verify Cart Badge
        expect(products_page.cart_badge).to_have_text("1")
        
        products_page.open_cart()

        # Cart
        cart_page = CartPage(page)
        expect(cart_page.get_cart_item(BACKPACK)).to_be_visible()
        
             
        # # Verify Product
        # expect(page.get_by_text("Sauce Labs Backpack")).to_be_visible()
        