import requests # requests는 요청 라이브러리
import pandas

res = requests.get('https://crix-api-cdn.upbit.com/v1/crix/candles/minutes/10?code=CRIX.UPBIT.KRW-ADT&count=400&ciqrandom=1582960162206')
data = res.json() # [{}, {}, {}]

saving = {
  "highPrice": [],
  "lowPrice": [],
  "openingPrice": [],
  "tradePrice": [],
}

for d in data:
  saving["highPrice"].append(d['highPrice'])
  saving["lowPrice"].append(d["lowPrice"])
  saving["openingPrice"].append(d["openingPrice"])
  saving["tradePrice"].append(d["tradePrice"])

df = pandas.DataFrame(saving)
df.to_csv('upbit_result.csv')