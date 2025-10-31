nombres = ["ana", "luis", "sofia", "pedro", "carla"]

for nombre in nombres:
    print(nombre)
    
print("nombres con mas de cuatro letras:")
for nombre in nombres:
    if len(nombre) > 4:
        print(nombre)