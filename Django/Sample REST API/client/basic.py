import requests

endpoint = "http://127.0.0.1:8000/api/products/"

response = requests.post(endpoint, json = {'query': 'Hello World!'})
print(response.json())

