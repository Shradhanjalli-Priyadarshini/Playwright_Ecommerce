from config.api_config import API_HEADERS
from config.auth_config import AUTH_HEADERS

class APIClient:

    def __init__(self, api_context, authenticated=False):
        self.api_context = api_context
        
        if authenticated:
            self.headers = AUTH_HEADERS
        else:
            self.headers = API_HEADERS

    def get_products(self):
        return self.api_context.get("/posts", headers=self.headers)

    def get_product_by_id(self, product_id):
        return self.api_context.get(f"/posts/{product_id}", headers=self.headers)

    def create_product(self, product_data):
        return self.api_context.post("/posts", data=product_data, headers=self.headers)

    def update_product(self, product_id, product_data):
        return self.api_context.put(
            f"/posts/{product_id}",
            data=product_data, headers=self.headers)

    def delete_product(self, product_id):
        return self.api_context.delete(f"/posts/{product_id}", headers=self.headers)
    
    def validate_status_code(self, response, expected_status):
        assert response.status == expected_status