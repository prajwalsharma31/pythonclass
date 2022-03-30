# a=(1,2,3,4,5,6)
# print(type(a))

#INSIDE TUPLE
#-INDEXED
#-ORDERED
#-DUPLICATE MEMBERS
#-IMUTABLE


# a=(1,2,3,4,5,6)
# b=("Apple","Ball","Cat","Dog","Fish")
# print(b[3])
# print(b)
# c=a+b
# print(c)


# -No Append()
# -No Extended
# -No Insert()
# -No Sort()
# -No Update
# -No del
# -No Remove
# -No Pop()


# a=(1,)
# print(a)
# type(a)


# a= tuple()
# b=("Apple",)
# print(a+b)


# y= tuple()
# n= int (input("Enter n = "))
# for i in range (n):
#     x=input("Enter x = ")
#     y= y+(x,)
# print(y)



# a= ('243', '234', '654', '234', '45')
# b= list(a)
# b.remove("243")
# a= tuple(b)
# print(a)



# def cal ():
#     a= 20
#     v= 40
#     return a,v
# cal()




# a={("Ram","Shyam"):98458524522}
# print(a)


# a={98458524522:("Ram","Shyam")}
# print(a)

# a= (1,2,3,4,5,2,3,433)
# print(sorted(a))


# a=[(1,2,3),(4,5,6),(7,8,9)]
# print(a)
# a.append((10,11,12))
# print(a)


a=([1,2,3],[4,5,6],[7,8,9])
b=([10,11,12],)
c=a+b
print(c)
a[0].append(4)
print(a)