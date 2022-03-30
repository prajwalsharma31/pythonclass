#List Inside List

# a= [[1,2,3],
#     [4,5,6],
#     [7,8,9]]
# b= [[],[],[]]
# print(a)
# print(type(a))

# a= [["ram",34,"kathmandu"],
#     ["shyam", 45, "patan"],
#     ["hari",67,"bara"]]
# print(a[0])

# a= [["ram",34,"kathmandu"],
#     ["shyam", 45, "patan"],
#     ["hari",67,"bara"]]
# print(a[0][0])

# a= [["ram",34,"kathmandu"],
#     ["shyam", 45, "patan"],
#     ["hari",67,"bara"]]
# for i in a:
#     print(i)


# info = list()
# n= int(input("Enter n = "))
# for i in range(n):
#     name = input("Enter name= ")
#     age= int(input("Enter age = "))
#     add= input("Enter add =")
#     data= [name,age,add]
#     info.append(data)
# print(info)


# info=[["ram",34,"karhmandu"],["shyam",45,"baluwatar"]]
# info.append(["hari",56,"janakpur"])
# print(info)


# info=[["ram",34,"karhmandu"],["shyam",45,"baluwatar"]]
# search = input("Enter search = ")
# for i in info:
#     if search in i:
#         print(i)
#         break
# else:
#     print("no data found")

# info=[["ram",34,"karhmandu"],["shyam",45,"baluwatar"]]
# info[0][0]="Ram"
# print(info)


# info=[["ram",34,"kathmandu"],["shyam",45,"baluwatar"]]
# info[0][0]=info[0][0].title()
# print(info)



# info=[["ram",34,"kathmandu"],["shyam",45,"baluwatar"]]
# del info[0]
# print(info)


# info=[["ram",34,"kathmandu"],["shyam",45,"baluwatar"]]
# del info[0][0]
# print(info)



# info=[["ram",34,"kathmandu"],["shyam",45,"baluwatar"]]
# len(info)
# print(len(info))



# m=[]
# r= int(input("Enter r = "))
# c= int(input("Enter c = "))
# for i in range(r):
#     n=[]
#     for j in range(c):
#         x= int(input("Enter x = "))
#         n.append(x)
#     m.append(n)
# print(m)



s=str()
n= int(input("enter n = "))
for i in range(n):
    name= input("enter name = ")
    phone = input("enter phone = ")
    s= s+f"{name}{phone}\n"
    print(s)
    s
a=s.split("\n")[0:-1]
print(a)
for i in a:
    print(i.split())


