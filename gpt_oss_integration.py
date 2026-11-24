import requests

def call_gpt_oss_api(data):
    url = "https://api.gpt-oss.com/v1/model"
    response = requests.post(url, json=data)
    return response.json()
