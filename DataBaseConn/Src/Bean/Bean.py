from Src.DAO.DAOIMPL import FetchData

#project8
class showDetails(FetchData):
    def __init__(self):
        super().__init__()
        print("child")
    
c=showDetails()
chapter=input("Enter the chapter Name: ")
c.FetchDataInputFromUser(chapter)
    
    
    #cFetch=FetchData()
    #chapter=input("Enter the chapter Name: ")
    #def FetchDataInputFromUser(self,chapter):
       
    #cFetch.FetchDataInputFromUser(chapter)
    
    