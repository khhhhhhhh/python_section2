from bs4 import BeautifulSoup
import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

from bs4 import BeautifulSoup
html = """
<html><body>
  <ul>
    <li><a href="http://www.naver.com">naver</a></li>
    <li><a href="http://www.daum.net">daum</a></li>
    <li><a href="https://www.google.com">google</a></li>
    <li><a href="https://www.tistory.com">tistory</a></li>
  </ul>
</body></html>
"""
soup = BeautifulSoup(html, 'html.parser')
# print('prettify',soup.prettify())들여쓰기 해서 정리해줌
a = soup.find_all("a", string="daum")
b = soup.find_all(string=["naver", "daum"])#진짜로 스트링만 가져옴
c = soup.find_all("a", limit=2)#limit로 2개만 가져옴
print('a',a)
print('b',b)
print('c',c)
links = soup.find_all("a")
print('links',links)
# 출력
for a in links:
    print('a',type(a),a)
    href = a.attrs['href']#attrs[키]로 가져옴,href가 키인거고 url이 벨류인듯 딕셔너리로 저장하는가보
    text = a.string#태그사이에 존재하는 내용을 가져오는듯?
    print(text, ">", href)
