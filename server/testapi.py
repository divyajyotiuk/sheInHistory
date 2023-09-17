import requests

url = 'http://localhost:3000/api/location'

# Assuming you want to retrieve data for the state "Florida"
params = {'state': 'Florida'}

response = requests.post(url, params=params)
print(response)
if response.status_code == 200:
    print("Data:", response.json())
else:
    print("Error:", response.status_code, response.text)

