from bs4 import BeautifulSoup
import urllib.request as req
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

url="https://news.daum.net/"#실제 웹페이지의 url입력받고



res=req.urlopen(url).read()#가지고온 url을 읽어들여서 객체로 만들고 urlopen을통해

soup=BeautifulSoup(res,'html.parser')#bs4를 통해 html파일을 가공하고 운용할수있게 만들어주기
soup1=soup.select("ol.list_popcmt>li>a>href")
for e in soup1:
 print(e)
