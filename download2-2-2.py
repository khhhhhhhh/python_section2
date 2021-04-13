#urllib을 이용해 데이터 추출하기(1)

import sys
import io
import urllib.request as dw#라이브러리?

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

print('안녕')

imgUrl="https://search.pstatic.net/common/?src=http%3A%2F%2Fblogfiles.naver.net%2FMjAyMDA5MjFfNTYg%2FMDAxNjAwNjg1NzczNzU4.Ki4FtgDEFG0kgqfhZ4F-IeG62D40LyYS-_KowX3EYfIg.RhOwZtnrNVte91XM6u6QjYfwDS2Xv-VdpW3NapvDsA8g.JPEG.gabin0529%2Fdusan-smetana-ZXuDkw7Be7E-unsplash.jpg&type=sc960_832"
htmlURL= "http://google.com"#웹경로

savePath1='c:/test1.jpg'   #내 컴퓨터 경로
savePath2="c:/index.html"

#사자의 모든사진을 다운받고싶을때
f=dw.urlopen(imgUrl).read()   #변수할당(웹파일)
f2=dw.urlopen(htmlUrl).read()

saveFile1=open(savePath1,'wb' )#w,r,a(데이터의 끝부분 추가할떄) #변수할당 내 경로
saveFile1.write(f)
saveFile1.close()

with open(savePath2,'wb') as saveFile2:#with는 close()가 항상 실행됨
    saveFile2.write(f2)

print("다운로드 완료")




#urlretrieve:저장 후 ->오픈-> 변수할당->파싱->
#urlopen: 저장을 하기전 메모리 변수할당-> 파싱-> 저장
