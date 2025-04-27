import pytest
import requests
import time

BASE_URL = "http://127.0.0.1:5000"

def test_login_success():
    response = requests.post(f"{BASE_URL}/login", json={"username": "admin", "password": "password123"})
    assert response.status_code == 200
    assert "token" in response.json()

def test_login_failure():
    response = requests.post(f"{BASE_URL}/login", json={"username": "admin", "password": "wrongpass"})
    assert response.status_code == 401

def test_profile_access():
    login_resp = requests.post(f"{BASE_URL}/login", json={"username": "admin", "password": "password123"})
    token = login_resp.json()["token"]
    
    profile_resp = requests.get(f"{BASE_URL}/profile", headers={"Authorization": f"Bearer {token}"})
    assert profile_resp.status_code == 200
    assert profile_resp.json()["username"] == "admin"

def test_profile_unauthorized():
    profile_resp = requests.get(f"{BASE_URL}/profile", headers={"Authorization": "Bearer wrongtoken"})
    assert profile_resp.status_code == 403

def test_performance_login():
    start_time = time.time()
    for _ in range(50):
        response = requests.post(f"{BASE_URL}/login", json={"username": "admin", "password": "password123"})
        assert response.status_code == 200
    duration = time.time() - start_time
    print(f"50 logins took {duration:.2f} seconds")
