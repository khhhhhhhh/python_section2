import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

class Warehouse:
    stock_num=0#클래스 변수라고 하는데 이것은 공유
    def __init__(self,name):
        self.name=name
        Warehouse.stock_num +=1

    def __del__(self):
        Warehouse_.stock_num-=1

user1=Warehouse('kim')#인스턴스 변수는 공유 안돰
user2=Warehouse('park')


print(user1.name)
print(user2.name)
print(user1.__dict__)
print(user2.__dict__)
print(Warehouse.__dict__)#인스턴스 네임페이스 확인->클래스 네임페이스 확인,클래스 변수 (공유)

print(user1.stock_num)
