'''
Created on 08-Mar-2024

@author: samar
'''
import mysql.connector as mysql

class Utils:
    
    
    def __init__(self):
        print("constr")
        
        
    def connection(self):
                                
                    db = mysql.MySQLConnection(
                    host="localhost",
                    user="samar",
                    passwd="Xorail@12345",
                    database="ExaminationDepartment_db"
                    )
                    
                    return db

