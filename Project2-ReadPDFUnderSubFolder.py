import PyPDF2 as PDF
import os  
import re
import glob   
#pdf_path=r"C:UsersDellDesktopTesting Tesseractexample.pdf"
pdf_path=r"/home/samar/Samar_PDF/content"
txt_path=r"/home/samar/Samar_PDF/content/text.txt"

global pdfdetais

def readFilePDF():
       
    
        try :
            
            #pdf_File_Object = open(pdf_path, 'rb')               
            
            #pdf_Reader = PDF.PdfReader(pdf_File_Object)
               
            
            #print("No. of pages in the given PDF file: ", len(pdf_Reader.pages))  
               
            
            #page_Object = pdf_Reader.pages[0] 
               
            
            #pdfdetais= "PDf ReadData \n"+ page_Object.extract_text()
            #print("Pdf: "+page_Object.extract_text())  
            
            #readText(pdfdetais)   #read read and write text file
            
            #pdf_File_Object.close() 
            
            
            for root, dirs, files in os.walk(pdf_path):
                #print(dirs)
                #print(files)
                #for file in glob.glob(pdf_path + "/*.pdf"):
                for file1 in dirs:
                    
                        print(file1)
                        for file in glob.glob(pdf_path+"/"+file1 + "/*.pdf"):
                                folderPath=pdf_path+"/"+file1
                                print(file)      
                                if file.endswith('.pdf'):
                                    #fileReader = PDF.PdfFileReader(open(file, "rb"))
                                    fileReader = PDF.PdfReader(open(file, "rb"))
                                    count = 0
                                    #count = fileReader.numPages
                                    #count =len(fileReader.pages)
                                    
                                    #while count >= 0:
                                        #count -= 1
                                    pageObj = fileReader.pages[count]
                                    text = pageObj.extract_text()
                                    print(text)
                                    num = re.findall(r'[0-9]+', text)
                                    print(num)
                                    readText(text,folderPath)
                                else:
                                        print("not in format")
            
            
            
            
            
        except FileNotFoundError:
            print("file not found")
        except IOError:
            print("file not found")
            
   
def readText(pdfdetais,txt_path):
    
    try:
         print("txt_path:"+txt_path)
         L = ["This is Delhi \n", "This is Paris \n", "This is London \n"] 
         newTextPath=txt_path+"/myfile.txt"  
         file1 = open(newTextPath, "w")
     
         print("Output of Read function is ")
         
         
         file1.write("Write in txt file \n")
         file1.writelines(L)
         file1.writelines(pdfdetais)
         #print("text file :"+file1.read())
         file2 = open(newTextPath, "r+")
         
         
         print("Output of Write function is ")
         print("After write text file :"+file2.read())
         
         file1.close()
         file2.close()
         
        
    
    except FileNotFoundError:
        print("file not found")
    except IOError:
            print("Error in text read")

if ((os.path.exists(pdf_path))):
    readFilePDF()
else:
    print("File or Folder not found:")
             
  
  


 