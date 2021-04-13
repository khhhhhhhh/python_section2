from bs4 import BeautifulSoup
import urllib.parse as rep
import urllib.request as req
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

base="https://www.inflearn.com/"#실제 웹페이지의 url입력받고
quote=rep.quote_plus("courses")
print(quote)#유니코드로 바꾸는 과정
url=base+quote

res=req.urlopen(url).read()#가지고온 url을 읽어들여서 객체로 만들고 urlopen을통해

soup=BeautifulSoup(res,'html.parser')#bs4를 통해 html파일을 가공하고 운용할수있게 만들어주기

# print(soup)


recommand=soup.select("div.course_title")#div라는 태그의 class가course_title인 애를 파싱
# print(recommand)

for i,e in enumerate(recommand,1) :
    print("인프런 추천강좌",i,e.string)#핵심은 내가 가져올 대상이 html으로 어떻게 구성이 되어있는가
