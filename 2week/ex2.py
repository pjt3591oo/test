import bs4 # 문자열을 파이썬에서 사용 가능한 객체(데이터 타입)으로 변환
import requests

res = requests.get('https://search.naver.com/search.naver?where=kin&sm=tab_jum&query=%ED%8C%8C%EC%9D%B4%EC%8D%AC')
soup = bs4.BeautifulSoup(res.content)
items = soup.select('#elThumbnailResultArea li') # select, 조회, 데이터 좀 주세요. # 리스트를 만들어 서 줌.

for item in items:
  title = item.select('dl dt a')[0].text
  print(title)