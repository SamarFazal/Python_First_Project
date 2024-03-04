import PPDF2 as PDF  
       
# Here we will create a pdf file object  
pdf_File_Object = open('exp.pdf', 'rb')  
       
    # Here, we will creat a pdf reader object  
pdf_Reader = PDF.PdfFileReader(pdf_File_Object)  
       
    # Now we will print number of pages in pdf file  
print("No. of pages in the given PDF file: ", pdf_Reader.numPages)  
       
    # Here, create a page object  
page_Object = pdf_Reader.getPage(0)  
       
    # Now, we will extract text from page  
print(page_Object.extractText())  
       
    # At last, close the pdf file object  
pdf_File_Object.close()  