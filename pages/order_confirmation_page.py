from pages.base_page import BasePage


class OrderConfirmationPage(BasePage):

    def __init__(self, page):

        super().__init__(page)

        self.complete_header = (
            self.page.get_by_text(
                "Thank you for your order!"
            )
        )

        self.complete_message = (
            self.page.get_by_text(
                "Your order has been dispatched"
            )
        )

        self.back_home_button = (
            self.page.get_by_role(
                "button",
                name="Back Home"
            )
        )

    def go_back_home(self):

        self.back_home_button.click()