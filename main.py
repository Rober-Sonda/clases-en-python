import player, transporte

Sorcerer = player.Sorcerer(vida=200, mana =5000)
caballero = player.Knight(vida=1000, mana =500)
paladin = player.Paladin(vida=500, mana=1000)
druida = player.Druida(vida=150, mana=6500)

print(Sorcerer)
print()
print(caballero)
print()
print(paladin)
print()
print(druida)
print()
avion = transporte.Avion(marca="Boeing",modelo="777",tipotransporte="Avion",navegacion="Aereo")
print(avion)
