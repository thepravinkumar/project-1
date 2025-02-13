import requests

BASE_URL = "http://127.0.0.1:8000"

def test_read_file():
    response = requests.get(f"{BASE_URL}/read?path=data/format.md")
    assert response.status_code == 200

def test_run_task():
    response = requests.post(f"{BASE_URL}/run?task=format markdown")
    assert response.status_code == 200
