# https://developer.pubg.com/
# must install requests package.
# find player_id from nickname.

from email.mime import base
import requests
import json

api_key = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJqdGkiOiJjNmM4YmQ5MC1iZjdmLTAxM2EtODMyMi00ZDEyNzA1YmVhZmEiLCJpc3MiOiJnYW1lbG9ja2VyIiwiaWF0IjoxNjUzNjEwNDE2LCJwdWIiOiJibHVlaG9sZSIsInRpdGxlIjoicHViZyIsImFwcCI6Imluc3RhbnQtc3R1ZHktIn0.6faRyUOGrdSJN6PkcQc6uBoAq5e8rYX30AO3he-BYr0"

header = {
    "Authorization": "Bearer {}".format(api_key),
    "Accept": "application/vnd.api+json",
}


def getPlayerIdFromPlayerNames(_player_name):
    player_id_r = requests.get(
        "https://api.pubg.com/shards/steam/players?filter[playerNames]={}".format(
            _player_name
        ),
        headers=header,
    )
    player_id = json.loads(player_id_r.text)["data"][0]["id"]
    return player_id


def playerStatus(_player_id):
    player_status_r = requests.get(
        "https://api.pubg.com/shards/steam/players/{}/seasons/lifetime/".format(
            _player_id
        ),
        headers=header,
    )
    player_status = json.loads(player_status_r.text)["data"]["attributes"]["gameModeStats"]
    print(player_status)
    return player_status


playerStatus(getPlayerIdFromPlayerNames("SonOfDongdo"))
