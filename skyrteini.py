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

fileName = 'felagaskirteini-'
documentTitle = 'Félagaskirteini - '
title = 'Félagaskirteini Íslenska alpaklúbbsins'
image = 'isalplogo.png'
year = 2020

# Reiknar og gefur unique ID neðst í skjalið
def idCalc(count, line):
  firstThree = line[0][0:3]
  lastThree = line[0][3:6]
  midSec = int(firstThree) + int(lastThree)
  check = year - 2000
  return 'ISALP' + str(count) + str(midSec) + str(check)

with open('test.csv') as csv_file:
  # Lesa skrá og hoppa yfir fyrstu línu
  csv_reader = csv.reader(csv_file)
  next(csv_reader)
  counter = 0
  # Útbúa PDF Skjöl
  for line in csv_reader:
    # Setja nafn á skjalið og haus
    counter = counter + 1
    pdf = canvas.Canvas(fileName + line[1] + '.pdf')
    pdf.setTitle(documentTitle + line[1])
    drawMyRuler(pdf)
    pdf.setFont('Courier', 26)
    pdf.drawCentredString(300,770,'Félagaskírteini')
    pdf.drawCentredString(300,720,'Íslenska alpaklúbbsins')
    pdf.line(30,710,550,710)

    pdf.setFont('Courier', 18)
    pdf.drawCentredString(300,680, '2020-2021')

    # Setja Ísalp logo á skjalið
    pdf.drawInlineImage(image, 150, 350,300,300)

    # Setja nafn og kennitölu inn í skjalið
    pdf.setFont('Courier', 12)
    pdf.drawString(50,300,line[1] + ', kt:' + line[0] + ' er meðlimur í Íslenska alpaklúbbnum')

    # Afsláttarkjör
    pdf.drawString(50, 250, 'Framvísun þessa skírteinis veitir afslátt á eftirfarandi stöðum:')

    pdf.setFont('Courier', 10)
    pdf.drawString(50, 100, idCalc(counter,line))
    print(counter)
    pdf.save()
    print(line)