
def verificar_poker():
    
  mano = []

  for i in range(5):
      valor = input("Ingrese el valor de la carta (A, 2, 3...J, Q, K,): ")
      carta = valor
      mano.append(carta)    
    
  hay_poker = False
  valor_poker = ""

  for carta in mano:
    valor = carta[0]
    contador = 0
    for otra in mano:
        if otra[0] == valor:
            contador = contador + 1
    if contador == 4:
        hay_poker = True
        valor_poker = valor

  if hay_poker:
    print(f"Hay poker de {valor_poker}")
  else:
    print("no hay poker")    
    
verificar_poker()                