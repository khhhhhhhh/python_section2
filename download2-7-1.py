from bs4 import BeautifulSoup
import urllib.request as req
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

url="https://finance.daum.net/"
res=req.urlopen(url).read()
soup=BeautifulSoup(res,'html.parser')
#
# print('soup',soup.prettify())
#
# top=soup.select("ul#mytopmylistmo1>li")
# print(top)
# for i,e in enumerate(top,1) :
#     print('e',e.find("a").string)#e의 type을 스트링으로 변환 해서 데이터를 추출해야함 ,find는 태그의 정보를 추출해오는 메소드인듯
