'''
Created on 10-Mar-2024

@author: samar
'''
#project8
from Database.Utils import Utils
from _mysql_connector import MySQLError

class FetchData:
    
    def __init__(self):
        print("")
        
    a="samar"
    global db
    db=Utils.connection(a)
    
    
    def FetchDataInputFromUser(self,chapter):
        
        c = db.cursor()
        
        try:
            
 
            # select statement for tblemployee which returns all columns
            #tableExamDetails_select = "SELECT * FROM TableExamDetails where Chapter_name='"+chapter+"'"
            tableExamDetails_select = "SELECT Question_Text FROM TableExamDetails where Chapter_name='"+chapter+"'"
                 
                # execute the select query to fetch all rows
            c.execute(tableExamDetails_select)            
            count = 0
            exam_data = c.fetchall()
                            
            for e in exam_data:
                count=1                         
                print(e)   
            
            
            if count==0:             
                print("Data not found")
                  
            db.close()
        
        except MySQLError as r:                
            print("Error in connection ",r)
        except Exception as e:
            print("Exception ",e)   
        
        

     

