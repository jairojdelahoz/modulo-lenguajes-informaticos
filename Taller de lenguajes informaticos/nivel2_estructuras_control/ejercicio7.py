number = int(input("Ingresa un numero: "))

if number <= 1: print("no es primo")
else:
    is_cousin = True
    for i in range(2, number):
        if number % i == 0:
            is_cousin = False
            break
    if is_cousin:
        print("es primo")
    else: 
        print("no es primo")