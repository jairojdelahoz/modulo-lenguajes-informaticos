word = input("Ingresa cualquier palabra: ").lower()
inverted_word = word[::-1]
if inverted_word == word:
    print("La palabra es palíndromo")
else: print("La palabra no es políndromo")