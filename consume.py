import requests
response = requests.get('http://127.0.01:8000/drinks')
print(response.json())
