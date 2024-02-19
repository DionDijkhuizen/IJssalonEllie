#imports
from helper import *
from presentatie import *
import csv

#dictionary inkomsten
inkomsten= {"Aardbeien-ijs-totaal": 1000, 
            "Vanille-ijs-totaal": 2000, 
            "Chocolade-ijs-totaal" : 1500, 
            "Waterijsjes-totaal" : 750 
            }

#Totaal inkomsten
totaal_inkomsten = som(inkomsten)

print()
print(totaal_inkomsten)
print()

# Presenteer totaal
presenteer(inkomsten, totaal_inkomsten)

#csv
with open('boekhouding.csv', 'w', newline='') as csvfile:
    for key, value in inkomsten.items():
        writer = csv.writer(csvfile,delimiter=';')
        writer.writerow([key,value])