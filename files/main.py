# b= open("file_name","<mode>")
# b.close()

#with open (<file_name>,<modes>) as file:
#<operations>

#TYPES OF MODES
# read -> r
# write -> m
# create -> x
# append -> a


# try:
#     b=open("data.txt","x")
#     b.close()
# except:
#     print("the file is already there")




# n= (input("Enter no of line = "))
# file = open("data.txt","r")
# for i in range(1,n+1):
#     if n!= i:
#         file.readline()
#     else:
#         print(file.readline())
#         break
# b.close()




# s=str()
# n=int(input("enter n= "))
# for i in range(n):
#      product=input("enter product name= ")
#      price=int(input("enter price= "))
#      quantity=int(input("enter quantity= "))
#      total=price*quantity
#      s=s+f"{product} {price} {quantity} {total}\n"
# print(s)
#
# with open("bill.txt","a") as file:
#     file.write(s)




# s=str()
# n=int(input("enter n= "))
# b= open("bill.csv","a")
#
# for i in range(n):
#      product=input("enter product name= ")
#      price=int(input("enter price= "))
#      quantity=int(input("enter quantity= "))
#      total=price*quantity
#      s=s+f"{product}, {price} ,{quantity} ,{total}\n"
#
# b.write("product , price , quantity,total \n")
# b.write(s)
# b.close()



import pandas as pd
df=pd.read_csv ("bill.csv")
print(df)



