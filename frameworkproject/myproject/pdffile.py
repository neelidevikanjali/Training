import PyPDF2

file = open('page.pdf', 'rb')
reader = PyPDF2.PdfFileReader(file)
page1 = reader.getPage(0)
print(reader.numPages)
pdfData = page1.extractText()
print(pdfData)

