from helper import *

inkomsten= {"Aardbeien-ijs-totaal": 1000, 
            "Vanille-ijs-totaal": 2000, 
            "Chocolade-ijs-totaal" : 1500, 
            "Waterijsjes-totaal" : 750 
            }

print()

for a in inkomsten:
    print(a)

print()

Totaal = sum(inkomsten.values())
print(Totaal)

print()

print(som(inkomsten))


