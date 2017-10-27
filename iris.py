import matplotlib.pyplot as plt
import numpy as np
import csv as csv

sepalLenghts =[]
sepalWidths = []
petalLenghts =[]
petalWidths = []
species = []

with open ('IRIS.csv') as irisCSV:
    readCSV = csv.reader(irisCSV, delimiter =',')

    for row in readCSV:
        sepalLenght = row[0]
        sepalWidth = row[2]
        
        sepalLenghts.append(sepalLenght)
        sepalWidths.append(sepalWidths)

		
plt.scatter(sepalLenghts,sepalWidths, label='IRISScatter', color = 'b')

plt.xlabel('SepalLenghts')
plt.ylabel('SepalWidths')
plt.title('Super Awesome Title for IRIS Graph')
plt.legend()
plt.show()