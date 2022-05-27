# https://developer.pubg.com/
# must install requests package.
# find player_id from nickname.

import requests
import json

url = "https://api.pubg.com/shards/steam/players?filter[playerNames]=Yonggumong"
api_key = "<your_api_key>"

header = {
    "Authorization": "Bearer {}".format(api_key),
    "Accept": "application/vnd.api+json",
}

r = requests.get(url, headers=header)
print("Bearer {}".format(api_key))
print(type(r))
print(json.loads(r.text))
