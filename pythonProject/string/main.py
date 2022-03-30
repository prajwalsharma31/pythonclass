

# # a="hello world"
# # print(a)
# # print(type(a))
#
#
# # a="hello"
# # b="world"
# # c=a+b
# # print(c)

# a="hello world\n"
# print(a*2)


# a="hello world"
# print(a[0])
# print(a[0:5])
# print(a[0:10:2])
# l=len(a)
# print(l)


# a="hello world"
# l=len(a)
# print(a[l::-1])


# a="hello world"
# l=len(a)
# print(a[l-1])

# a="hello world"
# l=len(a)
# print (a[0:100])


# name="ram"
# age="20"
# add="kathmandu"
# info =name+str(age)+add
# print(info)

#string FOrmating

# name="ram"
# age="20"
# add="kathmandu"
# info =f" hello i am {name}. i am{age}. i am from{add}."
# print(info)

# s=str()
# n=int(input("enter n= "))
# for i in range(n):
#     name=input("enter name=")
#     phone=input("enter phone=")
#     s=s+f"{name} {phone}\n"
#     print(s)


# s=str()
# n=int(input("enter n= "))
# for i in range(n):
#     product=input("enter product name= ")
#     price=int(input("enter price= "))
#     quantity=int(input("enter quantity= "))
#     total=price*quantity
#     s=s+f"{product} {price} {quantity} {total}\n"
# print(s)


#search
# name=input("enter name= ")
# a="Ram Shyam Hari Sita Ram Shyam Sita Rita"
# if name in a:
#     print("yes")
#     print(a.count(name))


#upper()  Lower()
# a="Hello WOrld"
# print(a.upper())
# print(a.lower())

# a="Ram Shyam Hari Sita Ram Shyam Sita Rita"
# print(a.replace("Ram","Rama"))
# print(a)


a="Ram Shyam Hari Sita Ram Shyam Sita Rita".lower()
a=a.replace("ram","Rama")
a=a.title()
print(a)