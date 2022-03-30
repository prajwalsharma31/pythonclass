#Dictionary
#- Indexing
#-Duplicate and Multiple values
#-Ordered
#-Multiable (multiple value)

# a={}
# b= dict{}
#a= {<key>:<value>,<key>:<value>,.....}


# a={"a":"apple","b":"ball","c":"cat"}
# b={1:1,2:4,3:9,4:16}
# print(a,b)
# print(a["a"])
# print(len(a))
# print(len(b))


# a={"a":"apple","b":"ball","c":"cat"}
# for i in a:
#     print(i)



# a={"a":"apple","b":"ball","c":"cat"}
# for i in a .values():
#     print(i)


# a={"a":"apple","b":"ball","c":"cat"}
# for i in a .items():
#     print(i)


# a={"a":"apple","b":"ball","c":"cat","A":"Apple"}
# print(a)


# a={"A":"apple","b":"ball","c":"cat","A":"Ant"}
# print(a)


# a={}
# a["a"]="Apple"
# a["b"]="Ball"
# a["c"]="Cat"
# print(a)


# d=dict()
# n=int(input("Enter n = "))
# for i in range(n):
#     name =input("Enter name = ")
#     phone= input("Enter phone = ")
#     d[name]=phone
#
# print(d)



#del  pop()

# a={"ram":6986455,"shyam":654561}
# del a["ram"]
# print(a)



# a={"ram":6986455,"shyam":654561}
# a.pop("ram")
# print(a)


# a={"ram":6986455,"shyam":654561}
# b=a.pop("ram")
# print(a)
# print(b)



# a={"ram":6986455,"shyam":654561}
# a.clear()
# print(a)


# a={"ram":6986455,"shyam":654561}
# b={"hari":98548522}
# a.update(b)
# print(a)


#List Inside DIctionary

# a={"ram":[6986455,98155525256524],"shyam":[654561,9854452452442]}
# print(a)



# d=dict()
# n=int(input("Enter n = "))
# for i in range(n):
#      name =input("Enter name = ")
#      ntc_phone=int(input("Enter ntc phone = "))
#      ncell_phone = int(input("Enter ncell phone = "))
#      d[name]=[ntc_phone,ncell_phone]
#
# print(d)



# d=dict()
# n=int(input("Enter n = "))
# for i in range(1,n+1):
#      name =input("Enter name = ")
#      age=int(input("Enter age = "))
#      address=(input("Enter address = "))
#      d[i]=[name,age,address]
#
# print(d)


# a={"name":["ram","shyam"],"age":[34,35],"Address":["kathmandu","bara"]}
# print(a)




# na=[]
# ag=[]
# add=[]
# n=int(input("Enter n = "))
# for i in range(1,n+1):
#      name =input("Enter name = ")
#      age=int(input("Enter age = "))
#      address=(input("Enter address = "))
#      na.append(name)
#      ag.append(age)
#      add.append(address)
#
# info={"name":na,"age":ag,"address":add}
# print(info)




# d= {"ram":[6986455,98155525256524],"shyam":[654561,9854452452442]}
# for i in d.items():
#     print(i)
# print(d["ram"][0])  #ntc number update
# d["ram"][0]=9585452654122
# print(d)


# a={"name":["ram","shyam"],"age":[34,35],"Address":["kathmandu","bara"]}
# a["name"].append("hari")
# a["age"].append(45)
# a["Address"].append("pokhara")
# print(a)


# data= {'name': ['ram', 'shyam', 'hari'], 'age': [34, 35, 45], 'Address': ['kathmandu', 'bara', 'pokhara']}
# name=input("Enter name = ")
# index=data["name"].index(name)
# print(index)


data= {'name': ['ram', 'shyam', 'hari'], 'age': [34, 35, 45], 'Address': ['kathmandu', 'bara', 'pokhara']}
del data["name"][index]
del data["age"][index]
del data["Address"][index]
print(data)