import requests

def call_ollama_api(api_key, data):
    url = "https://api.ollama.ai/v1/model"
    headers = {"Authorization": f"Bearer {api_key}"}
    response = requests.post(url, headers=headers, json=data)
    return response.json()
