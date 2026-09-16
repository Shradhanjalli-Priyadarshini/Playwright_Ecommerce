from pages.base_page import BasePage

class ProductsPage(BasePage):
    
    def __init__(self, page):
        super().__init__(page)
        
        # self.page = page
        
        self.products_title = page.get_by_text("Products")
        self.product_items = page.locator(".inventory_item")

        self.cart_badge = page.locator(".shopping_cart_badge")

        self.cart_link = page.locator(".shopping_cart_link")

    def add_product_to_cart(self, product_name): # one reusable method, instead of creating different methods for each product, we can create a single method that takes the product name as an argument and adds it to the cart.   

        product = self.product_items.filter(has_text=product_name)

        product.get_by_role("button", name="Add to cart").click()

    def open_cart(self):

        self.cart_link.click()
        