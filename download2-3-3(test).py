import sys
import io
import urllib.request as req#라이브러리?
# from urllib.parse import urlencode
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

API='https://tvetamovie.pstatic.net/libs/1331/1331252/e10fb33c05e268463ef5_20210324093527596.mp4-pBASE-v0-f127898-20210324093739809.mp4'
# values= {
#       'eu':'EU10041889'
# }
# print('before',values)
# params=urlencode(values)
# print('after',params)

url=API
# print('요청url',url)


reqData=req.urlopen(url).read()
# print('출력',reqData)

saveePath2="c:/assignment1.mp4"# 내컴퓨터의 경로이자 파일
with open(saveePath2,'wb') as saveFile2:
    saveFile2.write(reqData)
