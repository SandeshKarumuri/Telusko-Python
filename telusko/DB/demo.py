import mysql.connector

mydb= mysql.connector.connect(host="localhost",port=3308,user="Sandesh",passwd="Sandesh",database="work")
print(mydb)
mycursor = mydb.cursor()
mycursor.execute("show databases")
for i in mycursor:
    print(i)
mycursor.execute("select * from student")
result = mycursor.fetchall()
for i in result:
    print(i)


