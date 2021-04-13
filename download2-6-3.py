from bs4 import BeautifulSoup
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')


fp=open("cars.html",encoding="utf-8")#html 파일을 담아서 넣고
soup = BeautifulSoup(fp, "html.parser")#다시 그파일을 bs4로 변환햐소 다른 변수에 넣기


def car_func(selector):#선택자를 파싱해주는 함수 만들기 작업
    print("car_func",soup.select_one(selector).string)

car_lambda=lambda q : print("car_lambda",soup.select_one(q).string)
car_func("#gr")#id gr로
car_func("li#gr")
car_func("ul>li#gr")#ul중에 id가gr인 애들 뽑아 오기
car_func("#cars>#gr")#id가 car인 자식중에 id가gr인 애들 뽑아오기
car_func("li[id='gr']")
print()


car_lambda("#gr")
car_lambda("li#gr")
car_lambda("ul>li#gr")
car_lambda("#cars>#gr")
car_lambda("li[id='gr']")

print(soup.select("li")[3].string)#select vs find 의 차이가 뭐지?
print("car_func",soup.find_all("li")[3].string)
