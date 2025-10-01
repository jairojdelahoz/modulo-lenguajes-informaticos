print("Calculadora Basica")
print("Opciones")
print("1. Suma")
print("2. Resta")
print("3. Multiplicacion")
print("4. Division")
option = int(input("Elige una opcion: "))

if option == 0:
    print("Opcion no valida") 
elif option  > 4:
    print("Opcion no valida")
else:
   number1 = float(input("Ingresen el primer numero: ")) 
   number2 = float(input("Ingresen el segundo numero: "))
   
   if option == 1:
    print(f"El resultado de la suma: {number1 + number2}") 
   elif option == 2:
    print(f"El resultado de la resta es: {number1 - number2}")
   elif option == 3:
    print(f"El resultado de la multiplicacion es: {number1 * number2}")
   else:
     if number2 != 0:
      print(f"El resultado de la divicion es: {number1 / number2}")
     else:
        print("No se puede dividir entre cero")

 
         
      
      