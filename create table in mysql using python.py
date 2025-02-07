'''#To create a  table in MYSQL using python interface

import mysql.connector
mydb = mysql.connector.connect(host='localhost',\
                                user='root',\
                                passwd="9b73jgni@",\
                                database='school')
mycursor = mydb.cursor()
mycursor.execute('create table student(rollno int(3) primary key, Name varchar(15),age int, city char(8))')'''
#To check whether the created table exists in mysql using python interface
import mysql.connector
mydb = mysql.connector.connect(host='localhost',\
                                user='root',\
                                passwd="9b73jgni@",\
                                database='school')
mycursor = mydb.cursor()
mycursor.execute('show tables')
for x in mycursor:
    print(x)
