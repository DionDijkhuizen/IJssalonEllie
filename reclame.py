def aanbieding_1(smaak,prijs,korting):
    d = prijs - prijs * korting
    print(f"Vandaag in de aanbieding: emmertje ijs (1 liter) in de smaak {smaak}, van {prijs} euro voor {d}0 euro.")

print(aanbieding_1("aardbei",4,0.1))

def inkomsten_totaal1 (inkomsten):
    t = sum(inkomsten)
    btw = t * float(0.09)
    print(f"Het totaal van alle inkomsten van deze week is {t} euro, waarover {btw} euro betaald dient te worden")

print(inkomsten_totaal1([220, 430, 125, 160, 205, 90, 345]))