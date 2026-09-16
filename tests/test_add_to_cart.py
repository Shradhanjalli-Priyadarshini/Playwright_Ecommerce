from playwright.sync_api import expect

from pages.products_page import ProductsPage
from pages.login_page import LoginPage

from data.users import STANDARD_USER
from data.products import BACKPACK


def test_add_backpack_to_cart(page, base_url):

    login_page = LoginPage(page)

    login_page.open(base_url)

    login_page.login(
        STANDARD_USER["username"],
        STANDARD_USER["password"]
    )

    products_page = ProductsPage(page)

    products_page.add_product_to_cart(BACKPACK)

    expect(
        products_page.cart_badge
    ).to_have_text("1")

    products_page.open_cart()