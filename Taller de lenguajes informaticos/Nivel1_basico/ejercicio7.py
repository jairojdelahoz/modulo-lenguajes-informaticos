number1 = int(input("Ingresa el primer numero: "))
number2 = int(input("Ingresa el segundo numero: "))
number3 = int(input("Ingresa el tercer numero: "))
if number1 >= number2 and number1 >= number3:
    print(f"{number1} es el numero mayor")
elif number2 >= number1 and number2 >= number3:
    print(f"{number2} es el numero mayor")
else: print(f"{number3} es el numero mayor")

