import mysql.connector as mysql
from Database.Utils import Utils
 
# connecting to the mysql server
#db = mysql.MySQLConnection(
#    host="localhost",
 #   user="samar",
#    passwd="Xorail@12345"
#)
#a="samar"
db= Utils.connection()
# cursor object c
c = db.cursor()
 
# executing the create database statement
c.execute("CREATE DATABASE ExaminationDepartment_db")
 
# fetching all the databases
c.execute("SHOW DATABASES")
 
# printing all the databases
for i in c:
    print(i)
c = db.cursor()
 
# finally closing the database connection
db.close()