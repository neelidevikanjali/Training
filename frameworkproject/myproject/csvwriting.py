# importing required modules
# import PyPDF2
#
# # creating a pdf file object
# pdfFileObj = open('example.pdf', 'rb')
#
# # creating a pdf reader object
# pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
#
# # printing number of pages in pdf file
# print(pdfReader.numPages)
#
# # creating a page object
# pageObj = pdfReader.getPage(0)
#
# # extracting text from page
# print(pageObj.extractText())
#
# # closing the pdf file object
# pdfFileObj.close()

# import xlrd
#
# # Give the location of the file
# loc = ("path of file")
#
# # To open Workbook
# wb = xlrd.open_workbook(loc)
# sheet = wb.sheet_by_index(0)
#
# # For row 0 and column 0
# print(sheet.cell_value(0, 0))

# import csv
# with open('innovators.csv', 'r') as file:
#     reader = csv.reader(file)
#     for row in reader:
#         print(row)
# import csv
# import requests
# f = requests.get('http://sample.com/file.csv')
# #f = open('path/to/csv_file', encoding='UTF8')
# t = f.iter_lines()
# data = csv.reader()

import csv
data = ["Month", "1958", "1959", "1960"]
x = [
 ["JAN", 340, 360, 417],
 ["FEB", 318, 342, 391],
 ["MAR", 362, 406, 419],
 ["APR", 348, 396, 461],
 ["MAY", 363, 420, 472],
 ["JUN", 435, 472, 535],
 ["JUL", 491, 548, 622],
 ["AUG", 505, 559, 606],
 ["SEP", 404, 463, 508],
 ["OCT", 359, 407, 461],
 ["NOV", 310, 362, 390],
 ["DEC", 337, 405, 432],
]
y = "years.csv"
with open(y, 'w') as work:
   z = csv.writer(work)
   z.writerow(data)
   z.writerows(x)





