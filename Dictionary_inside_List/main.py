# Dictionary Inside List

a=[{"name":"Ram","Age":34,"Address":"Kathmandu"},
   {"name":"Shyam","Age":44,"Address":"Lalitpur"},
   {"name":"Hari","Age":36,"Address":"Bara"}]
info =[]
n = int(input("Enter n = "))
for i in range(n):
    name= input("Enter name = ")
    age = int(input("Enter age = "))
    add = input("Enter add = ")
    data = {"name":name,"Age":age,"Address":add}
    info.append(data)
    print(info)
info[0] ["phone"]=9848568524522
print(info)



a=[{"name":"Ram","Age":34,"Address":"Kathmandu"},
   {"name":"Shyam","Age":44,"Address":"Lalitpur"}]
a.append({"name":"nabin" , "Age":13,"Address": Bhaktpur})
print(a)




