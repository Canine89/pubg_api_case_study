# https://developer.pubg.com/
# must install requests package.
# find player from player_id.

import requests
import json

url = "https://api.pubg.com/shards/steam/players?filter[playerIds]=account.0214d347fdfd463bb6acd699d656fb14"
api_key = "<your_api_key>"

header = {
    "Authorization": "Bearer {}".format(api_key),
    "Accept": "application/vnd.api+json",
}

r = requests.get(url, headers=header)
print("Bearer {}".format(api_key))
print(type(r))
print(json.loads(r.text))
