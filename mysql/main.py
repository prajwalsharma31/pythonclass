# import mysql.connector
# database = mysql.connector.connect(
#     host="localhost",
#     user="root",
#     password="",
#     database="class8ampython"
# )
# db=database.cursor()
#
#
# sql="SELECT * FROM student"
# db.execute(sql)
# result=db.fetchall()
# print(result)
# for x in result:
#     print(x)


# sql="INSERT INTO student(name, physics, chemistry, math, english, nepali, total, per, grade)
# VALUES ('5', 'hari', '78', '80', '91', '85', '96', '495', '96', 'A')"
# db.execute(sql)
# database.commit()




import mysql.connector
database = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="class8ampython"
)
db=database.cursor()
sql="INSERT INTO student(name, physics, chemistry, math, english, nepali, total, per, grade) VALUES ('5', 'hari', '78', '80', '91', '85', '96', '495', '96', 'A')"
db.execute(sql)
database.commit()
sql="DELETE FROM student WHERE sn = 1"
db.execute(sql)
result =db.fetchall()
for x in result:
    print(x)