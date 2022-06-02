# API와 첫 만남

다음은 PUBG API를 파이썬에서 사용하는 가장 간단한 예입니다. API가 뭔지 말하기 전에 API를 그냥 한 번 좀 훑어봅시다.

```{python}
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

print(json.loads(r.text))
```

파이썬 문법이 익숙하지 않다면 코드가 좀 부담스러울 순 있겠지만 우선 실행부터 해보죠. 위 코드를 실행하려면 파이썬 3.9 버전 이상이 컴퓨터에 설치되어 있어야 하고, `requests`라는 파이썬 패키지가 설치되어 있어야 합니다. 설치를 마친 후에 코드를 실행해 봅니다. 지금의 경우 희영 대리님을 위해서 `api_key`를 오픈해 두었는데 이건 결제에 해당하는 문제라서 개인이 받아서 써야 합니다. 다만 공부를 위한 문서이므로 그냥 오픈해 두었습니다.

> api_key의 경우 추후 설명하도록 하겠습니다.

잡다한 출력이 보일텐데 우리가 집중해서 볼 결과물은 `print(json.loads(r.text))`입니다. 실행 결과는 다음과 같습니다.

```
{'data': [{'type': 'player', 'id': 'account.451653fde28643e8a6ec78ec2cb6014e', 'attributes': {'name': 'Yonggumong', 'stats': None, 'titleId': 'pubg', 'shardId': 'steam', 'patchVersion': ''}, 'relationships': {'matches': {'data': [{'type': 'match', 'id': '3893a495-8651-4c48-9a63-9aff831fca06'}, {'type': 'match', 'id': '60c16ffb-7996-4401-99cb-1dce310c0016'}, {'type': 'match', 'id': 'c53c21b8-2dcc-44e8-92c9-a7acef6cec9d'}, {'type': 'match', 'id': 'c9e7ec6d-48cf-4fe0-869a-15b0e7d32225'}]}, 'assets': {'data': []}}, 'links': {'self': 'https://api.pubg.com/shards/steam/players/account.451653fde28643e8a6ec78ec2cb6014e', 'schema': ''}}], 'links': {'self': 'https://api.pubg.com/shards/steam/players?filter[playerNames]=Yonggumong'}, 'meta': {}}
```

흠... 출력 결과를 보면 좀 정신이 없을 겁니다. 근데 쫄 필요 없습니다. 찬찬히 보면 출력 결과는 { ... }의 구성입니다. 즉, 코드의 실행 결과로 파이썬의 딕셔너리가 나온겁니다. 자 그럼 다시 돌아가서 상황을 정리해 봅시다. 코드를 실행했고, 어디선가 딕셔너리 결과물이 나왔습니다. 이게 어떻게 가능할 수 있을까요?

바로 API 덕분입니다. API는 검색해 보면 애플리케이션 프로그래밍 인터페이스(Application Programming Interface)의 줄임말입니다. 애플리케이션, 프로그래밍은 익숙한 단어인데 인터페이스는 어색한 단어일 겁니다. 그러니 인터페이스만 이해하면 API의 뜻을 이해할 수 있습니다. 인터페이스는 쉽게 말하면 **A와 B 사이의 상호작용을 위한 어떤 것**입니다. 이걸 좀 설명해야 합니다. 우선 성질이 급한 희영 대리라면 코드를 더 보고 싶겠지만 그건 잠깐 멈추고 우리 이론을 잠깐 둘러보고 옵시다. 그래야 앞으로의 코드 설명이 의미가 있거든요. 그럼 이론을 좀 둘러보겠습니다.

## 리모컨과 인터페이스
실생활을 예로 들어보겠습니다. 희영 대리가 TV를 좋아할진 모르겠는데(TV 얘기를 거의 안하는 듯) TV를 보려면 희영 대리는 어떻게 하나요? 아마 리모컨을 찾을 겁니다. 왜냐면 TV랑 상호작용하려면 리모컨이 필요하니까요. 숫자 버튼을 누르면 채널 번호를 입력할 수 있고, 전원 버튼을 누르면 TV가 켜지거나 꺼지거나 합니다. 그러니까 리모컨이 희영 대리와 TV 사이에서 인터페이스 역할을 하는 겁니다.

![tv_remocon](./image/tv-remocon.jpg)

인터페이스는 상호작용의 윤활유 역할을 하므로 매우 유용합니다. 만약 리모컨이 없다면 TV를 어떻게 조작할 수 있을까요? 아마 기판에 어떤 전기 신호를 흘려야 뭔가가 동작하는 등의 전문 지식이 필요할 겁니다. 하지만 리모컨이라는 인터페이스가 있다면? 그런 건 몰라도 됩니다. 원하는 기능이 있는 버튼만 누르면 되거든요. 인터페이스가 있는 이유는 바로 이겁니다. 상호작용, 상호작용의 편리함. 이 두 가지를 기억하면서 다음 설명인 API로 넘어갑시다.

## API
이제 다시 API로 돌아옵니다. API는 아까 말했듯이 애플리케이션 프로그래밍 인터페이스입니다. 아까의 리모컨 결을 그대로 살려 다시 설명하자면 개발을 위한 리모컨입니다. 보통 API라고 하면 날씨 데이터, 지도 데이터, 공공데이터와 같은 데이터를 떠올리기 쉬운데 API는 이런 데이터만을 위한 건 아닙니다. 이를테면 네이버에는 이런 API도 있습니다.

![naver-api-cafe-join](./image/naver-api-cafe-join.png)

카페 항목을 보면 특정 네이버 카페에 가입하는 API가 보입니다. 뭔진 몰라도 `https://openapi.naver.com/v1/cafe/{clubid}/members/`를 사용하면 특정 네이버 카페에 가입할 수도 있는 겁니다. 네이버 카페에 가입하여 뭔가를 하는 프로그램을 만든다면 이 API의 기능이 유용할 겁니다. 다른 API도 봅시다. 이건 영화 진흥 위원회의 API입니다.

![movie-api](./image/movie-api.png)

아래의 응답 예시 중 JSON 항목을 웹 브라우저에 입력하면 이런 결과를 볼 수 있습니다. 항목을 자세히 보면 순위, 영화 제목 등등 여러 데이터를 볼 수 있습니다.

![](./image/movie-api-result-sample.png)

API를 통해 영화 진흥원 서버와 상호작용한 거죠. 그리고 이 역시도 데이터 크롤링이나 데이터 보관을 위한 서버 없이 간편하게 URL 요청 한 번으로 데이터를 얻을 수 있으므로 편리합니다. 이게 API입니다. 다음 글에서는 본격적으로 PUBG API를 사용하면서 API를 사용하는 패턴에 익숙해지도록 합시다.