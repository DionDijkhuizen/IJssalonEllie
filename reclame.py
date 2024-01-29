def aanbieding_1(smaak,prijs,korting):
    d = prijs - prijs * korting
    print(f"Vandaag in de aanbieding: emmertje ijs (1 liter) in de smaak {smaak}, van {prijs} euro voor {d}0 euro.")

print(aanbieding_1("aardbei",4,0.1))