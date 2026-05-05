import requests
import time

url = "http://127.0.0.1:5000/"

for i in range(8):
    response = requests.get(url)
    print(f"Request {i+1}: {response.status_code} - {response.json().get('message', 'Blocked')}")

print("\n--- Waiting 2 seconds to refill ---")
time.sleep(2)

response = requests.get(url)
print(f"Request 9: {response.status_code} - {response.json().get('message', 'Blocked')}")