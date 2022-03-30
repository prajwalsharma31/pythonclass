# python collection
# -list
# -tuple
# -dictionary
# -set

#LIST
# -Indexed
# -Ordered
# -Multiple and duplicate values
# -mutable

# a=list()
# l=["apple","ball","cat"]
# print(type(l))


# l=["apple","ball","cat","dog","fish"]
# print(l[0])
# print(l[-1])
# print(l[0:5])
# print(l[0:6:2])


# l=["apple","ball","cat","dog","fish"]  #ordered list
# print(l)


# l=["apple","ball","cat","dog","fish"]
# k=["Zebra"]
# print(l+k)


# l=["apple","ball","cat","dog","fish","apple","apple"]   #duplicate value
# print(l)


# l=["apple","ball","cat","dog","fish"]
# l[0]="ant"
# print(l)

# How to create a list
# a=[]
# b=["ball"]
# print(a+b)

# names=list()
# n=int(input("Enter n= "))
# for i in range(n):
#     x=input("Enter name= ")
#     names =names +[x]
# print(names)



# y=list()
# n=int(input("Enter n= "))
# for i in range(n):
#     x=int(input("Enter x= "))
#     y =y +[x]
# print(y)
# print("sum of the list= ",sum(y))
# print("max value of the list= ",max(y))
# print("min value of the list= ",min(y))
# y.sort()
# print(y)
# y.reverse()
# print(y)


# y=list()
# n=int(input("Enter n= "))
# for i in range(n):
#     x=int(input("Enter x= "))
#     y =y +[x]
# print(y)


#append
#insert
# extended



# x=["apple","ball","cat","dog"]
# x.append("fish")
# print(x)


# y=list()
# n=int(input("Enter n= "))
# for i in range(n):
#     x=(input("Enter x= "))
#     y.append(x)
# print(y)


# x=["apple","ball","cat","dog"]
# x.insert(1,"cat")
# print(x)

# x=["apple","ball","cat"]
# y=[1,2,3]
# x.extend(y)
# print(x)


# x=["apple","ball","cat","dog"]
# for i in x:
#     print(i)

# x=["apple","ball","cat","dog"]
# for i in x:
#     print(x)


# x=["apple","ball","cat","dog"]
# for i in x:
#     if i== "cat":
#         break
#     print(i)


# x=["apple","ball","cat","dog"]
# for i in x:
#     if i== "cat":
#         continue
#     print(i)


# x=["apple","ball","cat","dog","goat","zebra"]
# if "apple" in x:
#     print("yes",x.count("apple"))


#del, remove(), pop()
# x=["apple","goat","xray","ball","zebra"]
# del x[0]
# print(x)


# x=["apple","goat","xray","ball","zebra"]
# x.remove("apple")
# print(x)


# x=["apple","goat","xray","ball","zebra"]
#y=x.pop
# x.pop(2)
# print(x)
#print(y)

# x=["apple","goat","xray","ball","zebra"]
# x.index("xray")
# print(x.index("xray"))


# x=["apple","goat","xray","ball","zebra","xray"]
# l=len(x)
# for i in range(l):
#     if(x[i])=="xray":
#         print(i)


x=["apple","goat","xray","ball","zebra","xray"]
for i in x:
    if i=="xray":
        x.remove("xray")
print(x)

