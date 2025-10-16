print("Ingrese los elementos de la lista separado por espacios:")
lista = input().split( )
lista = [int(i) for i in lista]

k = int(input("Ingrese el valor de K: "))

#Clasificar en (menores, iguales y mayores)
def clasificar_lista(lista, k):
    
    menores = []
    iguales = []
    mayores = []
    
    for numero in lista:
        if numero < k:
            menores.append(numero)
        elif numero == k:
            iguales.append(numero)
        else:
            mayores.append(numero)
    
    print(f"Menores: {menores}")
    print(f"Iguales: {iguales}")
    print(f"Mayores: {mayores}")
    
clasificar_lista(lista, k)

#Devolver multiplos de "K"
def multiplos_de_k(lista, k):
    
    multiplos = []
    
    for numero in lista:
        if numero % k == 0:
            multiplos.append(numero)
            
    print(f"Los multiplos de K son: {multiplos}")
    
multiplos_de_k(lista, k)
    