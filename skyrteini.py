import csv
from reportlab.pdfgen import canvas

def drawMyRuler(pdf):
  pdf.drawString(100,810, 'x100')
  pdf.drawString(200,810, 'x200')
  pdf.drawString(300,810, 'x300')
  pdf.drawString(400,810, 'x400')
  pdf.drawString(500,810, 'x500')

  pdf.drawString(10,100, 'y100')
  pdf.drawString(10,200, 'y200')
  pdf.drawString(10,300, 'y300')
  pdf.drawString(10,400, 'y400')
  pdf.drawString(10,500, 'y500')
  pdf.drawString(10,600, 'y600')
  pdf.drawString(10,700, 'y700')
  pdf.drawString(10,800, 'y800')

fileName = 'felagaskyrteini'
documentTitle = 'Félagaskýrteini - '
title = 'Félagaskýrteini Íslenska alpaklúbbsins'
subTitle = 'The larges carnivours...'
image = 'isalplogo.png'
year = 2020

pdf = canvas.Canvas(fileName + '.pdf')
pdf.setTitle(documentTitle)
pdf.drawString(270,770,title)
drawMyRuler(pdf)
pdf.save()

def idCalc(count):
  check = count % (year - 2000)
  return 'ISALP001' + str(check)

with open('test.csv') as csv_file:
  csv_reader = csv.reader(csv_file)
  
  next(csv_reader)

  for line in csv_reader:
    pdf = canvas.Canvas(fileName + line[1] + '.pdf')
    pdf.setTitle(documentTitle + line[1])
    drawMyRuler(pdf)
    pdf.setFont('Courier', 26)
    pdf.drawCentredString(300,770,'Félagaskýrteini')
    pdf.drawCentredString(300,720,'Íslenska alpaklúbbsins')
    pdf.line(30,710,550,710)

    pdf.setFont('Courier', 18)
    pdf.drawCentredString(300,680, '2020-2021')

    pdf.setFont('Courier', 14)
    pdf.drawString(50,400,line[0] + ' er meðlimur í Íslenska alpaklúbbnum')

    pdf.drawInlineImage(image, 130, 400)

    pdf.setFont('Courier', 10)
    pdf.drawString(50, 100, idCalc(101))

    pdf.save()
    print(line)