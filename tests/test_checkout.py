import pytest

from playwright.sync_api import expect

from pages.login_page import LoginPage
from pages.products_page import ProductsPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from pages.order_confirmation_page import OrderConfirmationPage

from data.users import STANDARD_USER
from data.products import BACKPACK
from data.checkout_data import CHECKOUT_USER


@pytest.mark.smoke
@pytest.mark.checkout
def test_complete_checkout(
    page,
    base_url
):

    # 1. Login
    login_page = LoginPage(page)

    login_page.open(
        base_url
    )

    login_page.login(
        STANDARD_USER["username"],
        STANDARD_USER["password"]
    )

    # 2. Add Product
    products_page = ProductsPage(page)

    products_page.add_product_to_cart(
        BACKPACK
    )

    # 3. Verify Cart Badge
    expect(
        products_page.cart_badge
    ).to_have_text("1")

    # 4. Open Cart
    products_page.open_cart()

    # 5. Verify Product in Cart
    cart_page = CartPage(page)

    expect(
        cart_page.get_cart_item(
            BACKPACK
        )
    ).to_be_visible()

    # 6. Checkout
    cart_page.checkout()

    # 7. Enter Customer Information
    checkout_page = CheckoutPage(page)

    checkout_page.enter_customer_information(
        first_name=CHECKOUT_USER["first_name"],
        last_name=CHECKOUT_USER["last_name"],
        postal_code=CHECKOUT_USER["postal_code"]
    )

    # 8. Continue Checkout
    checkout_page.continue_checkout()

    # 9. Verify Product on Overview Page
    expect(
        checkout_page.get_overview_product(
            BACKPACK
        )
    ).to_be_visible()

    # 10. Finish Order
    checkout_page.finish_order()

    # 11. Verify Order Confirmation
    confirmation_page = (
        OrderConfirmationPage(page)
    )

    expect(
        confirmation_page.complete_header
    ).to_be_visible()