from pages.base_page import BasePage


class CartPage(BasePage):

    def __init__(self, page):

        super().__init__(page)

        self.cart_items = self.page.locator(
            ".cart_item"
        )

        self.checkout_button = (
            self.page.get_by_role(
                "button",
                name="Checkout"
            )
        )

    def get_cart_item(self, product_name):

        return self.cart_items.filter(
            has_text=product_name
        )

    def checkout(self):

        self.checkout_button.click()