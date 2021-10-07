import requests

# Base url for localhost
base_url = "http://127.0.0.1:8000/quotes"

request = requests.get(base_url)
req_content = request.json()

print(req_content)
print(req_content["quote"])
print(req_content["game"])
