import requests
import pytest

BASE_URL = "https://reqres.in/api"

def test_get_user():
    response = requests.get(f"{BASE_URL}/users/2")
    assert response.status_code == 200
    data = response.json()
    assert data["data"]["id"] == 2
    assert "email" in data["data"]

def test_create_user():
    payload = {
        "name": "morpheus",
        "job": "leader"
    }
    response = requests.post(f"{BASE_URL}/users", json=payload)
    assert response.status_code == 201
    data = response.json()
    assert data["name"] == "morpheus"
    assert data["job"] == "leader"

def test_update_user():
    payload = {
        "name": "morpheus",
        "job": "zion resident"
    }
    response = requests.put(f"{BASE_URL}/users/2", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert data["job"] == "zion resident"