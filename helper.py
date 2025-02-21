import os
import requests

api_key = os.environ.get("GROQ_API_KEY")

url = "https://api.groq.com/openai/v1/models"

def get_models():
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }

    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        json_data = response.json()
        for data in json_data.get('data'):
            yield data['id']
