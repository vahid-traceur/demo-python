import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="test"
)

mycursor = mydb.cursor()

# mycursor.execute("create table customers (name varchar(20), address varchar(255))")

# mycursor.execute("alter table customers add (id int auto_increment primary key)")

# sql = "insert into customers (name, address) values (%s, %s)"
# val = ('vahid', 'isfahan 281')

# mycursor.execute(sql, val)
# mydb.commit()

mycursor.execute('select * from customers')

myresult = mycursor.fetchall()

# mycursor.execute("show tables")

# for x in mycursor:
#     print(x)

for x in myresult:
    print(x)

# print(mycursor.rowcount, "record inserted.")
