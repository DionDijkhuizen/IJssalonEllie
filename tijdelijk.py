prijzen = {"aardbei": 3, "vanille": 4, "chocolade": 5}
for k, v in prijzen.items():
  print(k, v)
aanbieding = 4 * 0.8
prijzen = {"aardbei": 3, "vanille": aanbieding, "chocolade": 5}
for k, v in prijzen.items():
  print(k, v)
reclame_tekst = f"Vandaag in de aanbieding: vanille-ijs, 1 liter – slechts € {aanbieding}"
print(reclame_tekst)