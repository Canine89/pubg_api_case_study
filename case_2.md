# 더 의미 있는 정보 받아보기
이제 PUBG API로 조금 더 의미 있는 정보를 받아봅시다. `case_1.py`로 얻은 데이터는 유저의 기초 정보만 받아오고 있으므로 사실 그렇게 유용하지 않습니다. 

```
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
```

우선 코드를 따라 입력하고 실행해 보면 이런 결과가 나옵니다.

```
Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJqdGkiOiJjNmM4YmQ5MC1iZjdmLTAxM2EtODMyMi00ZDEyNzA1YmVhZmEiLCJpc3MiOiJnYW1lbG9ja2VyIiwiaWF0IjoxNjUzNjEwNDE2LCJwdWIiOiJibHVlaG9sZSIsInRpdGxlIjoicHViZyIsImFwcCI6Imluc3RhbnQtc3R1ZHktIn0.6faRyUOGrdSJN6PkcQc6uBoAq5e8rYX30AO3he-BYr0
<class 'requests.models.Response'>
{'data': [{'type': 'player', 'id': 'account.0214d347fdfd463bb6acd699d656fb14', 'attributes': {'titleId': 'pubg', 'shardId': 'steam', 'patchVersion': '', 'name': 'dudududu', 'stats': None}, 'relationships': {'assets': {'data': []}, 'matches': {'data': []}}, 'links': {'self': 'https://api.pubg.com/shards/steam/players/account.0214d347fdfd463bb6acd699d656fb14', 'schema': ''}}], 'links': {'self': 'https://api.pubg.com/shards/steam/players?filter[playerIds]=account.0214d347fdfd463bb6acd699d656fb14'}, 'meta': {}}
```