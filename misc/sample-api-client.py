import requests

class APIClient:
    def __init__(self, base_url, api_key):
        self.base_url = base_url
        self.api_key = api_key

    def get(self, endpoint, params=None):
        if params is None:
            params = {}
        params['key'] = self.api_key
        response = requests.get(f"{self.base_url}/{endpoint}", params=params)
        return response

# Example usage:
api_key = "your_api_key_here"
base_url = "https://api.example.com"
client = APIClient(base_url, api_key)
response = client.get("endpoint")
print(response.json())  # or whatever processing you need to do with the response