import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

# class UserInfo:
#     def set_info(self,name,phone):
#         self.name=name
#         self.phone=phone

    # def print_info(self):
    #     print("----------")
    #     print("Name:"+self.name)
    #     print("Phone:"+self.phone)
    #     print("----------")


# user1=UserInfo()
# user2=UserInfo()
#
# user1.set_info("kim","010-2183-9223")
# user2.set_info("park","010-3829-2932")
#
# user1.print_info()
# user2.print_info()


# print(user1.__dict__)

class UserInfo:
    def __init__(self,name,phone):
        self.name=name
        self.phone=phone
    def print_info(self):
            print("----------")
            print("Name:"+self.name)
            print("Phone:"+self.phone)
            print("----------")
    def __del__(self):
        print("delete!")

user1=UserInfo("kim","010-2183-9223")
user2=UserInfo("park","010-3829-2932")

# user1.set_info("kim","010-2183-9223")
# user2.set_info("park","010-3829-2932")

user1.print_info()
user2.print_info()
