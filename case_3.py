# https://developer.pubg.com/
# must install requests package.
# find player stats.

import requests
import json

url = "https://api.pubg.com/shards/steam/players/account.451653fde28643e8a6ec78ec2cb6014e/seasons/lifetime"
api_key = "<your_api_key>"

header = {
    "Authorization": "Bearer {}".format(api_key),
    "Accept": "application/vnd.api+json",
}

r = requests.get(url, headers=header)
print("Bearer {}".format(api_key))
print(type(r))
print(
    "Yonggumong kill: ",
    json.loads(r.text)["data"]["attributes"]["gameModeStats"]["duo"]["kills"],
)
print(
    "Yonggumong assist: ",
    json.loads(r.text)["data"]["attributes"]["gameModeStats"]["duo"]["assists"],
)
print(
    "Yonggumong headshot kill: ",
    json.loads(r.text)["data"]["attributes"]["gameModeStats"]["duo"]["headshotKills"],
)
print(
    "Yonggumong suicides: ",
    json.loads(r.text)["data"]["attributes"]["gameModeStats"]["duo"]["suicides"],
)
