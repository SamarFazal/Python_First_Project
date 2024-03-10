'''
Created on 08-Mar-2024

@author: samar
'''

from Database.Utils import Utils
from _mysql_connector import MySQLError

class createTable:
    
    def __init__(self):
        print("sama")
        
    
    a="samar"
    global db
    db=Utils.connection(a)
       
        
    def employeeTableCreation(self):
            
            try :
                # cursor object c
                    c = db.cursor()
                     
                    # create statement for tblemployee
                    employeetbl_create = """CREATE TABLE `employee_db`.`tblemployee` (
                      `empid` INT NOT NULL AUTO_INCREMENT,
                      `empname` VARCHAR(45) NULL,
                      `department` VARCHAR(45) NULL,
                      `salary` INT NULL,
                       PRIMARY KEY (`empid`))"""
                     
                    c.execute(employeetbl_create)
                     
                    c = db.cursor()
                     
                    # fetch tblemployee details in the database
                    c.execute("desc tblemployee")
                     
                    # print the table details
                    for i in c:
                        print(i)
                     
                     
                    # finally closing the database connection
                    db.close()
            except MySQLError:
                
                print("Error in connection")
 
cj=createTable()
b="Samar"                                  
cj.employeeTableCreation()       
        