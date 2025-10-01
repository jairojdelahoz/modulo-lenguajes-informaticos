word = input("Ingresa una palabra: ").lower()
volwes = 0
for letter in word:
    if letter in ["a", "e", "i", "o", "u"]:
       volwes += 1            
print(f"La palabra tiene {volwes} vocal(es)")       