from playwright.sync_api import Playwright
from utils.api_client import APIClient
from data.api_test_data import CREATE_PRODUCT_DATA, UPDATE_PRODUCT_DATA
import time

def test_get_products(api_context):

    api_client = APIClient(api_context)

    response = api_client.get_products()

    api_client.validate_status_code(response, 200)

    response_data = response.json()

    assert isinstance(response_data, list)
    assert len(response_data) > 0

    print("Status Code:", response.status)
    print("Number of records:", len(response_data))
    print("First record:", response_data[0])
    
def test_get_product_by_id(api_context):

    api_client = APIClient(api_context)

    response = api_client.get_product_by_id(1)

    assert response.status == 200

    response_data = response.json()

    assert response_data["id"] == 1
    assert "title" in response_data
    assert "body" in response_data
    assert "userId" in response_data

    print("Status Code:", response.status)
    print("Product/Post ID:", response_data["id"])
    print("Title:", response_data["title"])
    
def test_create_product(api_context):

    api_client = APIClient(api_context)

    product_data = {
        "title": "Automation Test Product",
        "body": "Created using Playwright API testing",
        "userId": 1
    }

    response = api_client.create_product(CREATE_PRODUCT_DATA)

    assert response.status == 201

    response_data = response.json()

    assert response_data["title"] == CREATE_PRODUCT_DATA["title"]
    assert response_data["body"] == CREATE_PRODUCT_DATA["body"]
    assert response_data["userId"] == CREATE_PRODUCT_DATA["userId"]
    assert "id" in response_data

    print("Status Code:", response.status)
    print("Created ID:", response_data["id"])
    print("Created Data:", response_data)

def test_update_product(api_context):

    api_client = APIClient(api_context)

    product_data = {
        "id": 1,
        "title": "Updated Automation Product",
        "body": "Updated using Playwright API testing",
        "userId": 1
    }

    response = api_client.update_product(1, UPDATE_PRODUCT_DATA)

    assert response.status == 200

    response_data = response.json()

    assert response_data["id"] == UPDATE_PRODUCT_DATA["id"]
    assert response_data["title"] == UPDATE_PRODUCT_DATA["title"]
    assert response_data["body"] == UPDATE_PRODUCT_DATA["body"]
    assert response_data["userId"] == UPDATE_PRODUCT_DATA["userId"]

    print("Status Code:", response.status)
    print("Updated ID:", response_data["id"])
    print("Updated Data:", response_data)

def test_delete_product(api_context):

    api_client = APIClient(api_context)

    response = api_client.delete_product(1)

    assert response.status == 200

    print("Status Code:", response.status)
    print("Product deleted successfully")
    print("Status Code:", response.status)
    print("Product deleted successfully")

    api_context.dispose()
    
def test_get_invalid_product(api_context):

    api_client = APIClient(api_context)

    response = api_client.get_product_by_id(9999)

    assert response.status == 404

    print("Status Code:", response.status)
    print("Invalid product ID handled correctly")
    
def test_get_products_response_headers(api_context):

    api_client = APIClient(api_context)

    response = api_client.get_products()

    assert response.status == 200

    content_type = response.headers.get("content-type")

    assert content_type is not None
    assert "application/json" in content_type

    print("Status Code:", response.status)
    print("Content-Type:", content_type)
    
def test_get_products_response_time(api_context):

    api_client = APIClient(api_context)

    start_time = time.perf_counter()

    response = api_client.get_products()

    end_time = time.perf_counter()

    response_time = (end_time - start_time) * 1000

    assert response.status == 200

    print("Response Time:", round(response_time, 2), "ms")

    assert response_time < 2000
    
def test_api_chaining_get_and_get(api_context):
    # 1. Get all posts
    response = api_context.get("/posts")

    assert response.status == 200

    posts = response.json()

    # 2. Extract an existing post ID dynamically
    post_id = posts[0]["id"]

    # 3. Use the extracted ID in the next API request
    detail_response = api_context.get(
        f"/posts/{post_id}"
    )

    assert detail_response.status == 200

    # 4. Validate the returned post ID
    post_details = detail_response.json()

    assert post_details["id"] == post_id