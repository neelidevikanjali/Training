import xlrd
location = "sample.xls"
wb = xlrd.open_workbook(location)
sheet = wb.sheet_by_index(0)
sheet.cell_value(0, 0)
print(sheet.ncols)
