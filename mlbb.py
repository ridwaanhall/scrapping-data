import requests
import json
url = 'https://mainlagiaja.com/ajax/games/check/mobile-legend'
user_id = input("Enter user ID : ")
zone_id = input("Enter zone ID : ")
data = {
    'user_id': user_id,
    'zone_id': zone_id
}
headers = {
    'Content-Type': 'application/x-www-form-urlencoded'
}
response        = requests.post(url, data=data, headers=headers)
parsed_response = json.loads(response.text)
if parsed_response['ok'] == False:
    name = ''
else:
    name = parsed_response['name']
print(f"message : {parsed_response['msg']}")
print(f"name    : {name}")
