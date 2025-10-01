fibonacci = [0, 1]
for f in range(2,20):
    fibonacci.append(fibonacci[f - 1] + fibonacci[f - 2] ) 

print(f"los primeros 20 numeros de la serie de fibonacci: {fibonacci}")