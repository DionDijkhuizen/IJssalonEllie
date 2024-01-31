def aanbieding_1(smaak,prijs,korting):
    d = prijs - prijs * korting
    print(f"Vandaag in de aanbieding: emmertje ijs (1 liter) in de smaak {smaak}, van {prijs} euro voor {d}0 euro.")
print(aanbieding_1("aardbei",4,0.1))
print()

def inkomsten_totaal1 (inkomsten):
    totaal = sum(inkomsten)
    bedrag = totaal * float(0.09)
    print(f"Het totaal van alle inkomsten van deze week is {totaal} euro, waarover {bedrag} euro betaald dient te worden")
print(inkomsten_totaal1([220, 430, 125, 160, 205, 90, 345]))
print()

def laag_en_hoog (mijn_lijst):
   hoogste = max(mijn_lijst)
   laagste = min(mijn_lijst)
   print([hoogste,laagste])
print(laag_en_hoog([220, 430, 125, 160, 205, 90, 345]))
print()

import statistics
def gemiddelde(mijn_lijst):
    mean = statistics.mean(mijn_lijst)
    print(mean)
print(gemiddelde([220, 430, 125, 160, 205, 90, 345]))
