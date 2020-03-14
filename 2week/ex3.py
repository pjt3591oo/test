import requests
import bs4

res = requests.post(
  'http://dart.fss.or.kr/corp/searchCorpL.ax', 
  data={
    "currentPage": "10",
    "searchIndex": "4"
  }
)

soup = bs4.BeautifulSoup(res.content)
items = soup.select('.table_scroll table tbody tr') # row를 추출

for item in items:
  columns = item.select('td') # 컬럼을 추출
  
  if len(columns) > 3: 
    office_name = columns[0].text
    ceo_name = columns[1].text
    code = columns[2].text
    desc = columns[3].text
    print(office_name, ceo_name, code, desc)

