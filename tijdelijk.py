from helper import decoreer

def print_aanbieding():
  Prijzen = {"aardbei": 3, "vanille": 4, "chocolade": 5}

  aanbieding = Prijzen["aardbei"] * 0.8

  reclame_tekst = f"Vandaag in de aanbieding: aardbei-ijs, 1 liter – slechts € {aanbieding}"
  reclame_tekst2 = reclame_tekst[:63]
  reclame_tekst3 = reclame_tekst2.upper()
  reclame_tekst4 = reclame_tekst3.split()

  for El in reclame_tekst4:
    if 4 >= len(El):
      print(El.lower())
    else:
      print(El.upper())

decoreer("aanbieding")
print_aanbieding()  