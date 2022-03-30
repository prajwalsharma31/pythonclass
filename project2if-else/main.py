# # if <condition>:
# #     <operations>
# #     elseif <condition>
# #     <operations>
# #     if ...:
# #         else
# #         <operations>
# #
# #<> <= >= ==!=
# a=10
# b=20
# print(a!=b)
# a=10
# b=20
# if a<b:
#     print("b is greater")
# elif a>b:
#     print("a is greater")
# else:
#     print("both are equal")
# #
# a=int (input("Enter int a = "))
# if a%2 == 0:
#     print("a is even")
# else:
#     print(" a is odd")

# a = int(input("Enter int a = "))
# if a>0:
#         print("a is positive")
# else:
#         print(" a is odd")
# simple_calculator
# a=int(input("enter a= "))
# b=int(input("enter b= "))
# o= input("enter + - * /")
# if o== "+":
#     print(a+b)
# elif o== "-":
#     print(a-b)
# elif o=="*":
#     print(a*b)
# elif o=="/":
#     print(a/b)
# else:
#     print("invaldi operator")
#and &
# or
# 1*0=0
# 0*1=0
# 0*0=0
# 1*1=1
#print (True and True )
#print(True and False)
 #simple_calculator
# a=int(input("enter a= "))
# b=int(input("enter b= "))
# o= input("enter + - * /")
# if o== "+":
#      print(a+b)
# elif o== "-":
#      print(a-b)
# elif o=="*":
#      print(a*b)
# elif (o=="/") and (b!=0):
#      print(a/b)
# elif (0=="/")and (b==0):
#     print ("The value of b can not be zero")
# else:
#      print("invaldi operator")
# a=60
# if a>60 or a==60:
#     print("first division")
#
# #nested-if
# if<condition>:
#     if<condition>:
#         <operations>
#     elif <condition>:
#         <operations>
#     else:
#         <operations>
a=int(input("enter a= "))
b=int(input("enter b= "))
o= input("enter + - * /")
if o== "+":
      print(a+b)
elif o== "-":
      print(a-b)
elif o=="*":
      print(a*b)
elif (o=="/"):
    if(b!=0):
      print(a/b)
    else:
        print ("The value of b can not be zero")
else:
      print("invaldi operator")