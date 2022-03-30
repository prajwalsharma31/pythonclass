# class hello:          #class
#     pass
#
# obj = hello()         #object



# class hello:
#     print("hello world")
#
# obj = hello()



# class hello:
#     def hello(self):
#         print("hello world")
#
# obj =hello()
# obj.hello()



# class hello:
#     @staticmethod
#     def hello():
#         print("hello world")
#
# obj =hello()
# obj.hello()



# class cal:
#
#     def cal(self,l,b):
#         a = l*b
#         print(a)
#     def volume (self, l,b,h):
#         v= l*b*h
#         print(v)
#
# obj = cal()
# obj.cal(10,2)
# obj.volume(10,5,2)





# class cal:
#     def __init__(self,l,b,h):
#         self.l =l
#         self.b=b
#         self.h=h
#
#     def cal(self):
#         a = self.l*self.b
#         print(a)
#     def volume (self):
#         v= self.l*self.b*h
#         print(v)
#
# obj = cal()
# obj.cal(10,2)
# obj.volume(10,5,2)




# class info:
# def _init_(self):
#     self.name = input("enter name = ")
#     self.age =input"enter age")
#     self.add =input("enter add")




#INHERITANCE


# class profile:
#     def __init__(self):
#         self.name = input("Enter name = ")
#         self.address = input("Enter address = ")
# class Hr (profile):
#     def info (self):
#         print(self.name,self.address)
# x = Hr()
# x.info()




# class profile:
#     def __init__(self,address):
#         self.address = address
#
# class Hr (profile):
#     def __init__(self,name,address):
#         self.name = name
#         profile. __init__(self,address)
#     def info (self):
#         print(self.name,self.address)
# x = Hr("Ram","Nepal")
# x.info()


# class A:
#     pass
# class B(A):
#     pass
# class C(B):
#     pass
# obj = C ()


# class A:
#     pass
# class B:
#     pass
# class C(A,B):
#     pass
# obj = C ()



# class Name:
#     def __init__(self,name):
#         self.name = name
#
# class Address:
#     def __init__(self,address):
#         self.address = address
# class Info(Name, Address):
#     def __init__(self,name ,address):
#         Name.__init__(self,name)
#         Address.__init__(self,address)
#     def info(self):
#         print(self.name,self.address)
# x =Info("Ram","Nepal")
# x.info()



# class Name:
#     def __init__(self,name):
#         self.name = name
#
# class Address:
#     def __init__(self,address):
#         self.address = address
# class Info(Name, Address):
#     def __init__(self,name ,address,age):
#         self.age = age
#         Name.__init__(self,name)
#         Address.__init__(self,address)
#     def info(self):
#         print(self.name,self.address,self.age)
# x =Info("Ram","Nepal", 66)
# x.info()



# class Name:
#     def __init__(self,name):
#         self.name = name


# class Address:
#     def __init__(self,name,address):
#         self.address = address
#         Name.__init__(self,name)
# class Info(Address):
#     def __init__(self,name ,address,age):
#         self.age = age
#         Address.__init__(self,name,address)
#     def info(self):
#         print(self.name,self.address,self.age)
# x =Info("Ram","Nepal", 66)
# x.info()
# print(x.name)



#PRIVATE  PUBLIC   PROTECTED



#public
# class info:
#     def __init__(self,name,age,address):
#         self.name = name
#         self.age = age
#         self.address = address
#
# obj = info("ram",34, "kathmandu")
#
# print(obj.name)
# print(obj.age)
# print(obj.address)




#PROTECTED
# class info:
#     def __init__(self,name,age,address):
#         self._name = name
#         self._age = age
#         self._address = address
#
# obj = info("ram",34, "kathmandu")
#
# print(obj._name)
# print(obj._age)
# print(obj._address)




#PRIVATE
# class info:
#     def __init__(self,name,age,address):
#         self.__name = name
#         self.__age = age
#         self.__address = address
#
# obj = info("ram",34, "kathmandu")
#
# print(obj._info__name)
# print(obj._info__age)
# print(obj._info__address)





# class profile:
#     def __init__(self):
#         self._name = input("Enter name = ")
#         self.__age = int(input("Enter age = "))
#         self.address = input("Enter address = ")
#
# class Hr(profile):
#     def info (self):
#         print(f"hello world i am {self._name}. i am from{self.address}. i am {self._profile__age}")
# x=





class Name:
    def __init__(self,name):
        self.name = name

class Address:
    def __init__(self,address):
        self.address = address
class Info( Address):
    def __init__(self,name,address,age):
        self.__age = age
        Address.__init__(self,name,address)
    def info(self):
        print(f"hello i am {self.name}. i am from {self.address}. i am {self.__age}")
x =Info("Ram","Nepal", 66)
x.info()
print(x.name)
print(x._address)
print(x._info__age)