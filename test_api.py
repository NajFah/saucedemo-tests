import pytest
from playwright.sync_api import APIRequestContext, expect

def test_get_users_list(playwright):
    request_context = playwright.request.new_context()
    response = request_context.get("https://reqres.in/api/users?page=2")
    
    expect(response).to_be_ok()
    body = response.json()
    assert body["page"] == 2
    assert len(body["data"]) > 0
    
    request_context.dispose()


def test_create_user(playwright):
    request_context = playwright.request.new_context()
    response = request_context.post(
        "https://reqres.in/api/users",
        data={"name": "Najim", "job": "QA Tester"}
    )
    
    assert response.status == 201
    body = response.json()
    assert body["name"] == "Najim"
    assert body["job"] == "QA Tester"
    
    request_context.dispose()


def test_get_nonexistent_user(playwright):
    request_context = playwright.request.new_context()
    response = request_context.get("https://reqres.in/api/users/23")
    
    assert response.status == 404
    
    request_context.dispose()