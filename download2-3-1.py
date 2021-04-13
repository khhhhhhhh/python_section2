#urllib을 활용한 데이터 추출2
import sys
import io
import urllib.request as req#라이브러리?
from urllib.parse import urlparse
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')


url='http://www.encar.com/'
mem=req.urlopen(url)


#print(type(mem))
# print(type({}))
# print(type([]))
# print(type(()))
#
# print('geturl',mem.geturl())#주소반환
# print('status',mem.status) #속성을 알려줌 #200,404,403,500
# print('headers',mem.getheaders())#리스트 형태로 url관련 속성들을 반환해줌


# print('info',mem.info())#url getheaders랑 비슷한 정보들을 보가좋개 반환
# print('code',mem.getcode())#status랑 비슷한 값 반환
# print('read',mem.read(50).decode("utf-8")) #read(가져올 정보의 양(데이터 수)? 설정 가능),euc-kr(옛날 사이트)
# print(urlparse('http://www.encar.com?test=test'))
