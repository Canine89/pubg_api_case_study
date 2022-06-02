# https://developer.pubg.com/
# must install requests package.
# find player_id from nickname.

import requests
import json

url = "https://api.pubg.com/shards/steam/players?filter[playerNames]=Yonggumong"
api_key = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJqdGkiOiJjNmM4YmQ5MC1iZjdmLTAxM2EtODMyMi00ZDEyNzA1YmVhZmEiLCJpc3MiOiJnYW1lbG9ja2VyIiwiaWF0IjoxNjUzNjEwNDE2LCJwdWIiOiJibHVlaG9sZSIsInRpdGxlIjoicHViZyIsImFwcCI6Imluc3RhbnQtc3R1ZHktIn0.6faRyUOGrdSJN6PkcQc6uBoAq5e8rYX30AO3he-BYr0"

header = {
    "Authorization": "Bearer {}".format(api_key),
    "Accept": "application/vnd.api+json",
}

r = requests.get(url, headers=header)
print("Bearer {}".format(api_key))
print(type(r))
print(json.loads(r.text))
print(type(json.loads(r.text)))
