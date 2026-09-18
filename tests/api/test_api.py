import os
import pytest
import time
from dotenv import load_dotenv
from playwright.sync_api import APIRequestContext, Playwright
from data.api_test_data import CREATE_POST_PAYLOAD, UPDATE_POST_PAYLOAD

load_dotenv()

@pytest.mark.api
def test_get_product(api_request):
    start_time = time.perf_counter()

    response = api_request.get("/posts/1")

    response_time = time.perf_counter() - start_time

    assert response.status == 200
    assert response_time < 2.0

    content_type = response.headers.get("content-type")
    assert content_type is not None
    assert "application/json" in content_type

    data = response.json()

    assert data["id"] == 1
    assert "title" in data
    assert "body" in data
    
@pytest.mark.api    
def test_create_post(api_request):
    response = api_request.post(
        "/posts",
        data=CREATE_POST_PAYLOAD
    )

    assert response.status == 201

    data = response.json()

    assert data["title"] == CREATE_POST_PAYLOAD["title"]
    assert data["body"] == CREATE_POST_PAYLOAD["body"]
    assert data["userId"] == CREATE_POST_PAYLOAD["userId"]

@pytest.mark.api    
def test_update_post(api_request):
    response = api_request.put(
        "/posts/1",
        data=UPDATE_POST_PAYLOAD
    )

    assert response.status == 200

    data = response.json()

    assert data["id"] == 1
    assert data["title"] == UPDATE_POST_PAYLOAD["title"]
    assert data["body"] == UPDATE_POST_PAYLOAD["body"]
    assert data["userId"] == UPDATE_POST_PAYLOAD["userId"]

@pytest.mark.api    
def test_delete_post(api_request):
    response = api_request.delete("/posts/1")

    assert response.status == 200
    
@pytest.mark.api    
def test_get_invalid_post(api_request):
    response = api_request.get("/posts/9999")

    assert response.status == 404

    response_body = response.text()

    assert response_body is not None

@pytest.mark.api    
def test_get_posts_by_user(api_request):
    response = api_request.get(
        "/posts",
        params={"userId": 1}
    )

    assert response.status == 200

    data = response.json()

    assert isinstance(data, list)
    assert len(data) > 0

    for post in data:
        assert post["userId"] == 1

@pytest.mark.api        
def test_get_post_with_auth_header(api_request, auth_headers):
    response = api_request.get(
        "/posts/1",
        headers=auth_headers
    )

    assert response.status == 200

    data = response.json()

    assert data["id"] == 1

@pytest.mark.api    
@pytest.mark.parametrize("post_id", [1, 2, 3])
def test_get_post_by_id(api_request, post_id):
    response = api_request.get(f"/posts/{post_id}")

    assert response.status == 200

    data = response.json()

    assert data["id"] == post_id
    assert "title" in data
    assert "body" in data