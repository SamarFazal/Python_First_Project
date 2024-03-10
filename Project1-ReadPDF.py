import PyPDF2 as PDF
import os  
import configparser 
import re  
#pdf_path=r"C:UsersDellDesktopTesting Tesseractexample.pdf"
pdf_path=r"/home/samar/Samar_PDF/content/dummy.pdf"
txt_path=r"/home/samar/Samar_PDF/content/text.txt"

global pdfdetais

def readFilePDF(pageNo):
       
    
        try :
            
            pdf_File_Object = open(pdf_path, 'rb')               
            
            pdf_Reader = PDF.PdfReader(pdf_File_Object)
               
            
            print("No. of pages in the given PDF file: ", len(pdf_Reader.pages)) 
            print(pageNo)
            print(pageNo<=len(pdf_Reader.pages))
            if pageNo<=len(pdf_Reader.pages) :
                                 
                if pageNo!="" and pageNo!=0 :  #project 3
                    
                    page_Object = pdf_Reader.pages[pageNo-1] 
                else :
                    page_Object = pdf_Reader.pages[0]
                     
                
                pdfdetais= "PDf ReadData \n"+ page_Object.extract_text()
                print("Pdf: "+page_Object.extract_text())  
                
                #project-4 Read regular expression from a config file and extract content

                config = configparser.ConfigParser()
                config.read('Test.cfg')
                
                pattern1=config['Regular Expression']['Pattern1']
                pattern2=config['Regular Expression']['Pattern2']

                pattern3=config['Regular Expression1']['Pattern3']
                pattern4=config['Regular Expression1']['Pattern4']
                
                #print(pattern2)
                #print(pdfdetais)
                pattern=pattern2
                print(pattern)
                #filterdCfg = re.findall(pattern, str(pdfdetais), re.MULTILINE | re.VERBOSE)
                filterdCfg = re.findall(pattern, str(pdfdetais))
                print(" Inside Pattern: ",re.search(pattern, str(pdfdetais)))
                #print(" Inside Pattern: ",x)
                print(" Inside Pattern: ",filterdCfg)
                #project-4 Read regular expression from a config file and extract content
                readText(filterdCfg)
                #readText(pdfdetais)   #read read and write text file
                
                pdf_File_Object.close()
            else :
                print("sequence index out of range")
                raise IndexError("sequence index out of range")
                 
        except FileNotFoundError:
            print("file not found")
        except IOError:
            print("file not found")
        except Exception:
            raise IndexError("sequence index out of range")
        
            
   

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
    pageNo=int(input(" Enter the PDF page no ")) #project 3
    readFilePDF(pageNo)
else:
    print("File or Folder not found:")
             
  
  


 