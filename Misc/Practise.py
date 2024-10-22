# class BankAccount:
#     bank_name = "HDFC"

    # def __init__(self, acc_no, name, __acc_balance):
    #     self.acc_no = acc_no
    #     self.name = name
    #     self.__acc_balance = __acc_balance
    #     self.transactions = []

    # @property
    # def deposit(self):
    #     return self.__acc_balance

    # @deposit.setter
    # def deposit(self, amount):
    #     self.__acc_balance += amount


# c = BankAccount(123456789, "Mark", 0)
# c.deposit = 1000
# c.deposit = 1000
# c.deposit = 1000
# print(c.deposit)
# print(c.__dict__)
# print(BankAccount.__dict__)


# class Points:
#     def __init__(self,a,b):
#         self.a=a
#         self.b=b

#     def __setattr__(self,item,newvalue):
#         if not(item=='a' and isinstance(newvalue,int)):
#             raise Exception
#         self.a=newvalue
#         if not (item=='b' and isinstance(newvalue,int)):
#             raise Exception
#         self.b=newvalue
# p=Points("25",30)

# class Company1:
#     __branch="Bangalore"
#     def __init__(self,__name,age):
#         self.__name=__name
#         self.age=age
#     def _details(self):
#         return f"Hello {self.__name} you are {self.age} years old"
#     def __hello(self):
#         return "hai"

# c=Company1("Bill",50)
# print(c.__dict__)
# print(c._details())
# # print(c.__hello())
# print(Company1.__dict__)

#################################################################################################################

# class Sample:
#     def __init__(self,a):
#         self.a=a

    # def apple(self):
    #     return "Hai Welcome to apple park"

    # def google(self):
    #     return "Hai welcome to Google HQ"

# class Sample1(Sample):
#     def __init__(self,a):
#         super().__init__(a)

    # def apple(self):
    #     return "Hai welcome to apple park Cali"
    # def apple(self):
    #     return "Apple"

    # def google1(self):
    #     super().google()

# s1=Sample(15)
# s=Sample1(10)
# # print(s.__dict__)
# # print(s1.__dict__)
# # print(s.apple())
# print(s.apple())



###################################################################################################
def attach_count_value(cls):
    setattr(cls,"count",25)
    return cls
def attach_some_func(cls):
    def some_func(*args,**kwargs):
        return "something"
    setattr(cls,"Greet",some_func())
    return cls

@attach_some_func
@attach_count_value
class Demo:
    def __init__(self):
        self.count+=10
d=Demo()
# print(d.count)
# print(Demo.count)
# print(Demo.__dict__)

@attach_count_value
@attach_some_func
class sample:
    def __init__(self,a):
        self.a=a

# s=sample(15)
# print(sample.__dict__)
# print(sample.Greet)

class sample:
    def __init__(self,a):
        self.a=a
    def apple(self):
        return "apple"
    def google(self):
        return "google"
class sample1:
    def __init__(self,b):
        self.b=b
    def apple(self):
        return "apple1"
    def google(self):
        return "google1"
class sample2:
    def __init__(self,c):
        self.c=c
    def apple(self):
        return "apple2"
    def google(self):
        return "google2"
class sample3(sample,sample1,sample2):
    def __init__(self,d):
        self.d=d
    # def apple(self):
        # return "apple3"
    # def google(self):
    #     return "google3"

# s=sample3("d")
# print(s.apple())

#####################################################################################
# Aggregation

class Company:
    def __init__(self,name,age,pay):
        self.name=name
        self.age=age
        self.pay=pay

    def details(self):
        return f"The emplyee is {self.name} and he is {self.age} years old"

class Pay:
    def __init__(self,emp):
        self.emp=emp

    def total_ctc(self):
        return self.emp.pay*12


# e1=Company("Mark",45,15000)
# p=Pay(e1)
# print(p.total_ctc())

class Sample:
    def apple(self):
        return "Apple Products"

class Updates:
    def __init__(self,obj):
        self.obj=obj
    def apple_Updates(self):
        return f"All the {self.obj.apple()} have got new Updates"
s=Sample()
upt=Updates(s)
print(upt.apple_Updates())

############################################################
#Composition
class Company:
    def __init__(self,name,age,pay):
        self.name=name
        self.age=age
        self.pay=pay

    def details(self):
        return f"The emplyee is {self.name} and he is {self.age} years old"

class Pay:
    def __init__(self,name,pay,age):
        self.emp=Company(name,pay,age)

    def total_ctc(self):
        return self.emp.pay*12

    def emp_details(self):
        return self.emp.details()


e1=Company("Mark",45,15000)
# p=Pay("Steve",55,1000)
# print(p.total_ctc())
# print(p.emp_details())

########################################################################################################################

from xlrd import open_workbook

def read_data():
    wb=open_workbook("D:/PYTHON/SANDEEP SIR CLASS/SELENIUM/EXCEL SHEET/sample.xls")
    ws=wb.sheet_by_name("employees")
    rows=ws.nrows
    d={}
    for i in range(1,rows):
        tempdata=ws.row_values(i)
        d[tempdata[0],tempdata[1]]=tempdata[2],tempdata[3]
    return d
# print(read_data())

names = ['apple', 'google', 'yahoo', 'amazon', 'facebook', 'instagram', 'microsoft', 'zomato']
# print(sorted(names))
word="helloworld"
# print(sorted(word))
prices = {'ACME': 45.23, 'AAPL': 612.78, 'IBM': 205.55, 'HPQ': 37.20, 'FB': 10.75 }
print(sorted(prices,key=lambda item:item[0]))