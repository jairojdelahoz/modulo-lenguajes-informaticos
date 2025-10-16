print("Ingrese los elementos del primer vector separado por espacios:")
v1 = input().split( )
v1 = [int(v) for v in v1]

print("Ingrese los elementos del segundo vector separado por espacios:")
v2 = input().split( )
v2 = [int(v) for v in v2]

#Hallamos el producto escalar de dos vectores
def producto_escalar(v1, v2):

 total = 0
 for i in range(len(v1)):
    total = total + v1[i] * v2[i]
 return total

if len(v1) == len(v2):
     resultado = producto_escalar(v1, v2)
     print(f"el resultado del producto escarar es:{resultado}")
else:
     print("Error: los vectores deben tener el mismo tamaño")
     

#Saber si dos vectores son ortogonales
def son_ortogonales(v1, v2):
    producto = producto_escalar(v1, v2)
    if producto == 0:
        print("Si son ortogonales")
    else:
        print("No son ortoganales") 

son_ortogonales(v1, v2)

#Saber si dos vectores son paralelos 
def son_pararelos(v1, v2):
    i = 0
    razon = None
    paralelos = True
    
    while i < len(v1):
        if v2[i] == 0:
            if v1[i] != 0:
                paralelos = False
                break
        else:
            r = float(v1[i]) / float(v2[i]) 
            if razon == None:
                razon = r
            elif r != razon:
                paralelos = False
                break
        i = i + 1
        
    if paralelos:
        print("Son paralelos")
    else: 
        print("No son paralelos")
    
son_pararelos(v1, v2)

             