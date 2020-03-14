import requests # requests는 요청 라이브러리

res = requests.get('https://crix-api-cdn.upbit.com/v1/crix/candles/minutes/10?code=CRIX.UPBIT.KRW-ADT&count=400&ciqrandom=1582960162206')
data = res.json() # [{}, {}, {}]

for d in data:
  print(d['highPrice'], d['lowPrice'], d['openingPrice'], d['tradePrice'])

print(len(data))