# a=[i for i in range(5)]
# print(a)


a={"Ram":45 ,"shyam":55 ,"hari":56 ,"sita":10}
b= {x for x in a.items() if x[1]==10}
print(b)