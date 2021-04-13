#urllib을 이용해 데이터 추출하기(1)

import sys
import io
import urllib.request as dw#라이브러리?

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

print('안녕')

imgUrl="https://search.pstatic.net/common/?src=http%3A%2F%2Fblogfiles.naver.net%2FMjAyMDA5MjFfNTYg%2FMDAxNjAwNjg1NzczNzU4.Ki4FtgDEFG0kgqfhZ4F-IeG62D40LyYS-_KowX3EYfIg.RhOwZtnrNVte91XM6u6QjYfwDS2Xv-VdpW3NapvDsA8g.JPEG.gabin0529%2Fdusan-smetana-ZXuDkw7Be7E-unsplash.jpg&type=sc960_832"
htmlURL= "http://google.com"#웹경로2
savePath='c:/test1.jpg'#내 컴퓨터 경로1
savePath2="c:/index.html"#내 컴퓨터 경로2
dw.urlretrieve(imgUrl,savePath)#(웹경로,저장경로(파일네임.확장자))
dw.urlretrieve(htmlURL,savePath2)
#사자의 모든사진을 다운받고싶을때

print("다운로드 완료")
