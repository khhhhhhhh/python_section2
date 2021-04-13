import sys
import io
import urllib.request as req#라이브러리?
from urllib.parse import urlencode
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

API='https://ssl.pstatic.net/tveta/libs/1320/1320372/cbd2ba27658b89a9e825_20210323162129422.jpg'
values= {
      'eu':'EU10041889'
     }
print('before',values)
params=urlencode(values)
print('after',params)

url=API+'?'+params
print('요청url',url)


reqData=req.urlopen(url).read()
print('출력',reqData)

saveePath2="c:/indexa.jpg"
with open(saveePath2,'wb') as saveFile2:
    saveFile2.write(reqData)
