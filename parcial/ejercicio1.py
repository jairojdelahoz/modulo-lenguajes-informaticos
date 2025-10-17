
number = int(input("Ingrese un numero entero positivo: ")) # le pedimos al usuario que ingrese el numero entero positivo
impares = [] #definimos una lista vacia
for x in range(number): # recoremos la lista
    if x%2 != 0: #comparamos si su modulo es diferente de cero
        impares.append(x) #agregamos el numero impar

print("los impares son:" , impares) #se imprimen los impares




print("ingrese la lista separada por comas: ") # le solicitamos al usuario ingresar la lista separada por comas
lista = input().split(",")  # creamos la lista con el metodo split(separa los elementos de la lista por el parametro dado (en este caso es ","))


new_lista = []  #definimos una lista vacia

for number in lista: #recoremos la lista creada con los datos ingresados por el usurio
    number = number.strip( ) # eliminamos los espacios del primer elemento 
    if number not in new_lista: #comparamos si el elemneto no este en la nueva lista
        new_lista.append(number) #agregamos el elemento
print(new_lista) # se imprime la lista sin duplicados


