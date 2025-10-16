carta = ('A', 'Corazones')

valores = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
palos = ['Corazones', 'Picas', 'Treboles', 'Diamantes']

baraja = [(valor, palo) for valor in valores for palo in palos]
print(baraja[:5])