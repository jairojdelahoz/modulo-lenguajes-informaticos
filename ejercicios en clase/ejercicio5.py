notas = [4,3,5,4,2] 
nota1,nota2,nota3,nota4,nota5 = notas
promedio = (nota1 + nota2 + nota3 + nota4 + nota5) / 5 
  
if promedio >= 3: print("el estudiante esta aprobado") 
else: print("el estudiante esta reprobado") 
  
print( "su promedio es: ",promedio) 
notas.sort()
print("sus notas son:", notas)