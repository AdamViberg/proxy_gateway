import requests

# The base URL of your FastAPI service
base_url = "http://127.0.0.1:8001/items/"

# Sending a GET request
response_get = requests.get(base_url)
print(f"GET Response: {response_get.json()}")

# Sending a POST request
# response_post = requests.post(base_url)
# print(f"POST Response: {response_post.json()}")
