print("Ingrese los elementos del vector separado por espacios:")
vector = input().split( )
vector = [int(v) for v in vector]

#Calcular la norma del vector
def norma(vector):
  suma = 0
  for v in range(len(vector)):
      suma = suma + vector[v] * vector[v]
      
  print("La norma del vector es: ", suma ** 0.5)
  
norma(vector)  

