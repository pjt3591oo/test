data = [
  {"time": "2020-03-14", "tradePrice": "10000000", "amount": "0.3", "price": "3000000"},
  {"time": "2020-03-14", "tradePrice": "10000000", "amount": "0.3", "price": "3000000"},
  {"time": "2020-03-14", "tradePrice": "10000000", "amount": "0.3", "price": "3000000"},
  {"time": "2020-03-14", "tradePrice": "10000000", "amount": "0.3", "price": "3000000"},
  {"time": "2020-03-14", "tradePrice": "10000000", "amount": "0.3", "price": "3000000"},
  {"time": "2020-03-14", "tradePrice": "10000000", "amount": "0.3", "price": "3000000"},
  {"time": "2020-03-14", "tradePrice": "10000000", "amount": "0.3", "price": "3000000"},
  {"time": "2020-03-14", "tradePrice": "10000000", "amount": "0.3", "price": "3000000"},
]

order = {
  "buy": {
    "9746000": ["0.1", "0.2", "0.3"],
    "9747000": ["0.1", "0.2", "0.3"],
    "9748000": ["0.1", "0.2", "0.3"],
    "9749000": ["0.1", "0.2", "0.3"],
    "9750000": ["0.1", "0.2", "0.3"],
  },
  "sell": {
    "9746000": ["0.1", "0.2", "0.3"],
    "9747000": ["0.1", "0.2", "0.3"],
    "9748000": ["0.1", "0.2", "0.3"],
    "9749000": ["0.1", "0.2", "0.3"],
    "9750000": ["0.1", "0.2", "0.3"],
  }
}

for item in data:
  print(item['time'], item['tradePrice'], item['amount'], item['price'])

buy= order['buy']
some_price = buy['9748000']
for od in some_price:
  print(od)

some_price.append('0.5')
some_price.append('0.6')
some_price.append('0.7')
print(order)

for od in some_price:
  print(od)