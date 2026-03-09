import requests

url = "https://catfact.ninja/fact"

response = requests.get(url)

print("Status Code :", response.status_code)
print("Response Content :", response.text)
