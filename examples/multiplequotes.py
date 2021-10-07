import requests
from typing import List


def make_request(number: int) -> List:
    # Base url for localhost
    base_url = f"http://127.0.0.1:8000/quotes/{number}"

    request = requests.get(base_url)
    req_content = request.json()

    return req_content


# Make request to the API
quotes = make_request(5)

# Print each fetched quote individualy
for i in quotes:
    print(quotes)
