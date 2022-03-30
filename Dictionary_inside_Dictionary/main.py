# # Function Calling on DIctionary  (Extra Bonus)
#
# def dict1():
#     d1={}
#     n= int(input("Enter n = "))
#     for i in range(n):
#         x=int(input("Enter value = "))
#         d1[x]=x*x
#     return d1
#
# def dict2():
#     d2={}
#     n= int(input("Enter n = "))
#     for i in range(n):
#         x=int(input("Enter value = "))
#         d2[x]=x*x
#     return d2
#
# x=dict1()
# y=dict2()
# x.update (y)
# print(x)



# a= {1:{"Name":"Ram","Age":34,"Address":"Kathmandu"},
#     2:{"Name":"Hari","Age":23,"Address":"Lalitpur"},
#     3:{"Name":"Shyam","Age":53,"Address":"Bara"}}
# print(a)
# a[1]["phone"]= 98452452255325
# a[2] ["phone"]=566461641
# a[3] ["phone"]=463126541
# print(a)
#
# del a[1]["phone"]
# print(a)



# Wap to create dictionary inside dictionary
info={}
n= int(input("Enter n = "))
for i in range(1,n+1):
    name=input("Enter name = ")
    age=int(input("Enter age = "))
    add=input("Enter add = ")
    data ={"name":name,"Age":age,"Address":"add"}
    info[i]=data
print(info)
