import csv
from reportlab.pdfgen import canvas

with open('test.csv') as csv_file:
  csv_reader = csv.reader(csv_file)
  
  next(csv_reader)

  for line in csv_reader:
    print(line)