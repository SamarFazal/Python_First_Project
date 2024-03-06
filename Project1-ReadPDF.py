import PyPDF2 as PDF
import os  
   
#pdf_path=r"C:UsersDellDesktopTesting Tesseractexample.pdf"
pdf_path=r"/home/samar/Samar_PDF/content/dummy.pdf"
txt_path=r"/home/samar/Samar_PDF/content/text.txt"

global pdfdetais

def readFilePDF():
       
    
        try :
            
            pdf_File_Object = open(pdf_path, 'rb')               
            
            pdf_Reader = PDF.PdfReader(pdf_File_Object)
               
            
            print("No. of pages in the given PDF file: ", len(pdf_Reader.pages))  
               
            
            page_Object = pdf_Reader.pages[0] 
               
            
            pdfdetais= "PDf ReadData \n"+ page_Object.extract_text()
            print("Pdf: "+page_Object.extract_text())  
            
            readText(pdfdetais)   #read read and write text file
            
            pdf_File_Object.close() 
        except FileNotFoundError:
            print("file not found")
        except IOError:
            print("file not found")
            
   

def readText(pdfdetais):
    
    try:
         L = ["This is Delhi \n", "This is Paris \n", "This is London \n"]   
         file1 = open(txt_path, "r+")
     
         print("Output of Read function is ")
         print("text file :"+file1.read())
         
         file1.write("Write in txt file \n")
         file1.writelines(L)
         file1.writelines(pdfdetais)
         
         file2 = open(txt_path, "r+")
         
         
         print("Output of Write function is ")
         print("After write text file :"+file2.read())
         
         file1.close()
         file2.close()
         
        
    
    except FileNotFoundError:
        print("file not found")
    except IOError:
            print("Error in text read")

if ((os.path.exists(pdf_path)) and (os.path.exists(txt_path))):
    readFilePDF()
else:
    print("File or Folder not found:")
             
  
  


 