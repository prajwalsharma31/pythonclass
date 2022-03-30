# # def <function_name>():
# #     <operations>
# # <function_name>()
#
# def hello():
#     print("Hello wprld")
# hello()

# def cal():
#     l=int(input("Enter the value of l="))
#     b=int(input("Enter the value of b="))
#     h=int(input("Enter the value of h="))
#     v=l*b*h
#     print(v)
# cal()

# def hello():
#     x= int(input("Enter x= "))
#     y= int(input("Enter y= "))
#     print(x+y)
# hello()


# def cal():
#     l=int(input("Enter the value of l="))  #local variable
#     b=int(input("Enter the value of b="))  #local variable
#     h=int(input("Enter the value of h="))  #local variable
#     v=l*b*h
#     print(v)
# cal()


# l=int(input("Enter the value of l="))  #local variable
# b=int(input("Enter the value of b="))  #local variable
# h=int(input("Enter the value of h="))  #local variable
# def cal():
#     v=l*b*h
#     print(v)
# cal()
# print(l,b,h)

# def cal():
#     global l,b,h
#     l=int(input("Enter the value of l="))  #local variable
#     b=int(input("Enter the value of b="))  #local variable
#     h=int(input("Enter the value of h="))  #local variable
#     v=l*b*h
#     print(v)
# cal()

#Function have two type
#Argument
#return type


# def area (l,b):
#     a=l*b
#     print(a)
# area(10,5)


# def cal(x,y,z):
#     v=x*y*z
#     print(v)
# l=int(input("Enter l= "))
# b=int(input("Enter b= "))
# h=int(input("Enter h= "))
# cal(l,b,h)


# l=int(input("Enter l= "))
# b=int(input("Enter b= "))
# h=int(input("Enter h= "))
# def cal(l,b,h):
#     v=l*b*h
#     print(v)
#
# cal(l,b,h)


# def language (lan= "python"):
#     print(lan)
# language("c++")
# language("C")
# language("java")
# language()


# def language (name="Shiva",lan= "python"):
#     print(name,lan)
# language("Ram","c++")
# language("Shyam","C")
# language("Hari","java")
# language("nabin")

#Return type function
# def cal():
#     l=10
#     b=5
#     a=l*b
#     return a
# print(cal())


# def cal():
#     l=10
#     b=5
#     a=l*b
#     return a
# x=cal()
# print(x)


# def cal():
#     l=10
#     b=5
#     h=3
#     a=l*b
#     v=a*h
#     return a,v
# x=cal()
# area,volume=x
# print(area)
# print(volume)
# print(x)

#furnction with argument and Return type

# def info (name,age,add):
#     s="hello my name is "+name+" i am from "+add+" i am "+str(age)
#     return s
# name=input("enter name= ")
# age=int (input("enter age= "))
# add=input("enter address= ")
# x=info(name,age,add)
# print(x)

# def area (l,b):
#     a=l*b
#     return a
# def volume(l,b,h):
#     v=area(l,b)*h
#     return v
# l=int(input("Enter l= "))
# b=int(input("Enter b= "))
# h=int(input("Enter h= "))
# print(volume(l,b,h))



# def add(a,b):
#     return a+b
# def sub(a,b):
#     return a-b
# def mul(a,b):
#     return a*b
# def div(a,b):
#     return a/b
# def cal():
#     a=int(input("enter a= "))
#     b=int(input("enter b= "))
#     o= input("enter + - * /")
#     if o== "+":
#       print(add(a,b))
#     elif o== "-":
#       print(sub(a,b))
#     elif o=="*":
#       print(mul(a,b))
#     elif (o=="/") and (b!=0):
#       print(div(a,b))
#     elif (0=="/")and (b==0):
#      print ("The value of b can not be zero.")
#     else:
#       print("invaldi operator")
# cal()


# def hello():
#      print("hello world")
#      x=input("Enter y for more call= ")
#      if x=="y":
#          hello()


# username="admin"
# password="admi123"
# def auth():
#     x=input("Enter username= ")
#     y=input("Enter password= ")
#     if x!=username and y!=password:
#         auth()
#     else:
#         print("you are loged in")
# auth()



# def signup():
#     print("--------please signup-------")
#     username=input("Enter username= ")
#     password=input("Enter password= ")
#     cpassword=input("Enter cpassword")
#     if cpassword==password:
#         return username,password
#     else:
#         print("password and confirm password is not same")
#         signup()
# username,password=signup()
# def auth():
#     print("------login------")
#     x=input("Enter username= ")
#     y=input("Enter password= ")
#     if x!=username and y!=password:
#         auth()
#     else:
#         print("you are loged in")
# auth()



#Math FUnction


# import math as m
# print(m.pi)
# print(m.e)
# r=




# import math as m
# r=int(input("enter r= "))
# a=m.pi*m.pow(r,2)
# print(a)


import math as m
m.factorial(5)