number = int(input("Ingresa un numero entero positivo: "))
counter = number - 1
while counter != 0:
    number = number * counter
    counter -= 1

print(number)