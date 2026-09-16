from pages.base_page import BasePage


class CheckoutPage(BasePage):

    def __init__(self, page):

        super().__init__(page)

        self.first_name_input = (
            self.page.get_by_placeholder("First Name")
        )

        self.last_name_input = (
            self.page.get_by_placeholder("Last Name")
        )

        self.postal_code_input = (
            self.page.get_by_placeholder("Zip/Postal Code")
        )

        self.continue_button = (
            self.page.get_by_role(
                "button",
                name="Continue"
            )
        )

        self.cart_items = self.page.locator(
            ".cart_item"
        )

        self.finish_button = (
            self.page.get_by_role(
                "button",
                name="Finish"
            )
        )

    def enter_customer_information(
        self,
        first_name,
        last_name,
        postal_code
    ):

        self.first_name_input.fill(first_name)
        self.last_name_input.fill(last_name)
        self.postal_code_input.fill(postal_code)

    def continue_checkout(self):

        self.continue_button.click()

    def get_overview_product(self, product_name):

        return self.cart_items.filter(
            has_text=product_name
        )

    def finish_order(self):

        self.finish_button.click()