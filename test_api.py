import requests

url = "http://127.0.0.1:8000/users"

response = requests.get(url)

print(response.json())
print(response.status_code)
print(response.headers)
print(response.text)