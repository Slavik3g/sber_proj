import requests
import json

API_URL = "http://127.0.0.1:8000/api"


def load_json_file(file_path):
    with open(file_path, "r", encoding='utf-8') as file:
        data = json.load(file)
    return data


def test_api_post_with_json_file():
    json_file_path = "../examples/example.json"
    payload = load_json_file(json_file_path)
    response = requests.post(f"{API_URL}/v1/parse_document", json=payload)
    expected_path = "../examples/output.json"
    expected_data = load_json_file(expected_path)
    assert response.status_code == 200, f"Expected status code 200, but got {response.status_code}"
    assert response.json() == expected_data
