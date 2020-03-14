orderbook = {
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

# sell 9751000 0.1

orderPrice=  '9750000'
orderAmount = '0.1'

# price = orderbook['sell'].get(orderPrice, 0)

# if price == 0:
#   print('not found price:', orderPrice)
#   orderbook['sell'][orderPrice] = []

orderbook['sell'].setdefault(orderPrice, []) # 22 ~ 26번줄의 기능과 동일함

orderbook['sell'][orderPrice].append(orderAmount)
print(orderbook['sell'])
# orderbook['sell']['9751000'].append(0.1)


# CRUD => Create, Read, Update, Delete
