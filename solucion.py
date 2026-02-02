#Ejercicio 1

num1 = input(float("Ingrese el primer número: "))
num2 = input(float("Ingrese el primer número: "))
suma = num1 + num2
print("La suma es", suma)

#ejercicio 2

num = input(int("Ingrese un número: "))
if num % 2 == 0:
    print("el número es par")
else: 
    print("El número es impar")

#Ejercicio 3

num = input(int("Ingrese un número: "))
for i in range(1, 11):
    print(num, "x", i, "=", num*i)


#Ejercicio 4

palabra = input("Ingrese la palabra: ")
print("La palabra tiene", len(palabra), "letras")