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
       
        
    def examTableCreation(self):
            
            try :
                # cursor object c
                    c = db.cursor()
                     
                    # create statement for tblemployee
                    examtbl_create = """CREATE TABLE  IF NOT EXISTS `ExaminationDepartment_db`.`TableExamDetails` (
                      `Id` INT NOT NULL AUTO_INCREMENT,
                      `Subject_Name` VARCHAR(45) NULL,
                      `Question_Text` VARCHAR(300) NULL,
                      `Answer_options` VARCHAR(300) NULL,
                      `Chapter_name` VARCHAR(300) NULL,
                       PRIMARY KEY (`Id`))"""
                     
                    c.execute(examtbl_create)
                     
                    c = db.cursor()
                     
                    # fetch tblemployee details in the database
                    c.execute("desc TableExamDetails")
                     
                    # print the table details
                    for i in c:
                        print(i)
                     
                    a="s";
                    insertDataInTable(a)
                    # finally closing the database connection
                    db.close()
            except MySQLError:                
                print("Error in connection")
                
                
                
                
def insertDataInTable(self):
            
            try :
                # cursor object c
                    c = db.cursor()
                     
                    # create statement for tblemployee
                    # this statement will enable us to insert multiple rows at once.
                    
                    
                    examtbl_insert = "INSERT INTO TableExamDetails (Subject_Name,Question_Text,Answer_options,Chapter_name)  VALUES  (%s, %s, %s, %s)"
                     
                    # we save all the row data to be inserted in a data variable
                    data = [
                                ('English', 'What do you want to drink?', 'We want some fruit juice.','Genral'),
                                ('GK', 'What did the earthquake damage?', 'The earthquake damaged my house.','Genral'),
                                ('GK', 'What causes cancer', 'Smoking causes cancer.','Genral')
                            ]
                     
                    # execute the insert commands for all rows and commit to the database
                    c.executemany(examtbl_insert, data)
                     
                    # print the table details
                    '''for i in c:
                        print(i)'''
                     
                    db.commit()
                    # finally closing the database connection
                    db.close()
            except MySQLError:
                
                print("Error in connection")
 
cj=createTable()                                 
cj.examTableCreation()       
        