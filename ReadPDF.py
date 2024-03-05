import PyPDF2 as PDF  
   
#pdf_path=r"C:UsersDellDesktopTesting Tesseractexample.pdf"
pdf_path=r"/home/samar/Samar_PDF/content/dummy.pdf"

try :
    #pdf_File_Object = open('exp.pdf', 'rb')  
    pdf_File_Object = open(pdf_path, 'rb')   
    # Here, we will creat a pdf reader object  
    #pdf_Reader = PDF.PdfFileReader(pdf_File_Object)
    pdf_Reader = PDF.PdfReader(pdf_File_Object)    
       
    # Now we will print number of pages in pdf file  
    #print("No. of pages in the given PDF file: ", pdf_Reader.numPages)
    print("No. of pages in the given PDF file: ", len(pdf_Reader.pages))  
       
    # Here, create a page object  
    #page_Object = pdf_Reader.getPage(1)
    page_Object = pdf_Reader.pages[0] 
       
    # Now, we will extract text from page  
    print(page_Object.extract_text())  
       
    # At last, close the pdf file object  
    pdf_File_Object.close() 
except FileNotFoundError:
    print("file not found")
    
    
        
# Here we will create a pdf file object  

 