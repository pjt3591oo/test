import requests
import bs4
import pandas

res = requests.post(
  'http://dart.fss.or.kr/corp/searchCorpL.ax', 
  data={
    "currentPage": "10",
    "searchIndex": "4"
  }
)

saving = {
  "office_name": [],
  "ceo_name": [],
  "code": [],
  "desc": []
}

soup = bs4.BeautifulSoup(res.content)
items = soup.select('.table_scroll table tbody tr') # row를 추출

for item in items:
  columns = item.select('td') # 컬럼을 추출
  
  if len(columns) > 3: 
    office_name = columns[0].text.replace('\n', '').replace('\r', '').replace('\t', '')
    ceo_name = columns[1].text.replace('\n', '').replace('\r', '').replace('\t', '')
    code = columns[2].text.replace('\n', '').replace('\r', '').replace('\t', '')
    desc = columns[3].text.replace('\n', '').replace('\r', '').replace('\t', '')
    saving['office_name'].append(office_name)
    saving['ceo_name'].append(ceo_name)
    saving['code'].append(code)
    saving['desc'].append(desc)

df = pandas.DataFrame(saving)
df.to_csv('dart.csv')