
import csv
with open('years.csv', 'r')as file:
   csv_rows = csv.reader(file)
   for row in csv_rows:
      print(row)

