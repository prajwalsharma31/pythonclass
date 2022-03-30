# # # # for loop
# # # # while loop
# # # start for loop
# # # range(5) #0,1,2,3,4
# # # range(1,5) #1,2,3,4
# # # range(1,5,2) #1,3
# # # for i in range(5): for(i=1; i<5;i++;)
# # #     print(i)
# # # for i in range(1,5,2):
# # #     print(i,"hello world")
# #
# # x=int (input("Enter x= "))
# # for i in range(1,11):
# #     print(x*i)
#
# # x=int (input("Enter x= "))
# # for i in range(1,11):
# #     print(x,"*",i,"=",x*i)
#
# # n= int(input("Enter n= "))
# # for i in range(2):
# #     x=input("Enter x= ")
# #     print(x)
#
# # s=0  #s mean sum
# # n= int(input("Enter n= "))
# # for i in range(n):
# #     x=int (input("Enter x= "))
# #     s= s+x
# #     print("sum is = " ,s)
#
# # s=str()  #s mean string
# # n= int(input("Enter n= "))
# # for i in range(n):
# #     x= input("Enter x= ")
# #     s= s+x+" "
# #     print("sum is = " ,s)
#
# # s=str()  #s mean string
# # n= int(input("Enter n= "))
# # for i in range(n):
# #     name = input("Enter name= ")
# #     phone = input("Enter phone=")
# #     s= s+name+" "+phone+"\n"
# #     print(s)
#
# # 4! =1*2*3*4
# # fac=1
# # n= int (input("Enter n= "))
# # for i in range(1,n+1):
# #     fac=fac*i
# #     print(fac)
#
# #control statement
# # break
# # continue
# # pass
#
# # a="hello world "  #vertical
# # for i in a:
# #     print(i)
#
# # a = "hello world "  # horizantal
# # for i in a:
# #         print(i, end="")
#
# a = "hello world i am python "
# for i in a:
#     if i!=" ":
#         print(i, end="")
#


# a = "hello world i am python "
# for i in a:
#     if i==" ":
#         print(i, end="")

#break
# for i in range(10):
#     if i==5:
#         break
#     print(i)

   #continious
# for i in range(10):
#     if i==5:
#         continue
#     print(i)

for i in range(1,51):
    if i%5 !=0:
        continue
    print(i)
