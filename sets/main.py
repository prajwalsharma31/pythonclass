#set


# a={1,2,3,4,5,6,7,8,9}
# print(type(a))


# IN  SET
# -NO INDEXING
# -UNORDERED
# -NO DUPLICATE VALUES
# -MUTABLE


# a={1,2,3,4,5,6,7,8,9}
# a[0]



# a={"apple","ball","cat","zebra","xray"}
# print(a)


# a={2323,242425,52562,55262,678}
# print(a)

# a={11,22,33,44,55,11,33,22,44}
# print(a)



# a=["Apple","Apple","Ball","Ball"]
# b=set(a)
# a=list(b)
# print(a)

# a={"xray","apple","ball","cat","zebra"}
# b={"fish"}
# a.update(b)
# print(a)


# a={"xray","apple","ball","cat","zebra"}
# a.remove("xray")
# print(a)


# abc={"Ram","Shyam","Hari","Sita","Gita"}
# xyz={"Hari","Sita","Nabin","Akash","Shyam"}
# union = abc.union(xyz)
# print(union)
#
# intersection = abc.intersection(xyz)
# print(intersection)


# abc={"Ram","Shyam","Hari","Sita","Gita"}
# xyz={"Hari","Sita","Nabin","Akash","Shyam"}
# difference = abc.difference(xyz)
# print(difference)
#
# difference = xyz.difference(abc)
# print(difference)



u={"Shyam","Sita","Hari","Nabin","Ram","Gita","Akash","Rabin","Sabin"}
abc={"Ram","Shyam","Hari","Sita","Gita"}
xyz={"Hari","Sita","Nabin","Akash","Shyam"}
union = abc.union(xyz)
difference = u.difference(union)
print(difference)