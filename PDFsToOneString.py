#! python3
#PDFsToOneString.py

import os
import PyPDF2

#Erstelle txt-File wo alles reinkommt
txtFile = open("Datastring.txt", "w")
txtFile.close()
txtFile = open("Datastring.txt", "ab")
#Gehe in den PDF Ordner
os.chdir("PDfs")

#try:
for file in os.listdir():
    if file.endswith(".pdf"):
        pdfFileObj = open(file, "rb")
        pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
        for i in range(pdfReader.numPages):
            pageObj = pdfReader.getPage(i)
            text = pageObj.extractText()
            txtFile.write(text.encode("utf-8"))
#except:
#    print("Error")
    
txtFile.close()
