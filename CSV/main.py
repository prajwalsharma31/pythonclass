# try:
#     b= open("data.csv","x")
#     b.close()
# except:
#     print("the file is already there")


# import pandas as pd
# df=pd.read_csv("data.csv",index_col="sn")
# print(df)



# import pandas as pd
# df=pd.read_csv("data.csv",index_col="sn")
# print(df.head())




# import pandas as pd
# df=pd.read_csv("data.csv",index_col="sn")
# print(df.tail())



# import pandas as pd
# df=pd.read_csv("data.csv",index_col="sn",usecols=["sn","Name","Phone"])
# print(df.tail())



# import pandas as pd
# df=pd.read_csv("data.csv",index_col="sn")
# print(df.iloc[1:4])



# import pandas as pd
# df=pd.read_csv("data.csv",index_col="sn")
# print(df.loc[1:4])



# import pandas as pd
# df=pd.read_csv("data.csv",index_col="Name")
# print(df.loc["Ram":"Sabin"])


# import pandas as pd
# df=pd.read_csv("data.csv",index_col="sn")
# print(df["Age"])


# import pandas as pd
# df=pd.read_csv("data.csv",index_col="Name")
# print (df [df["Age"]>40])



# import pandas as pd
# df=pd.read_csv("data.csv",index_col="Name")
# print (df [df["Address"]== "Kathmandu"])


# import pandas as pd
# df=pd.read_csv("data.csv",index_col="Name")
# data = (df [df["Age"]>40])
# data.to_csv("new_data.csv")

# import pandas as pd
# df=pd.read_csv("new_data.csv",index_col="sn")
# print(df)



#LIST INSIDE DICTIONARY

# import pandas as pd
# d={"Name":["Ram","Shyam","Hari"],
#    "Age":[13,45,63],
#    "Address":["Kathmandu","Chitwan","Bara"]}
# df= pd.DataFrame(d)
# print(df)
# #df.to_json("new_data.json")
# df.to_csv("datas.csv")



#WAP TO ENTER LIST INSIDE LIST IN TO CSV