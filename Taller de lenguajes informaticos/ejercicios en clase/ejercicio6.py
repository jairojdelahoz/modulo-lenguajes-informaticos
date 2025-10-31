productos = []
precios = []

# Pedir al usuario los nombres y precios de 5 productos
for i in range(5):
    nombre = input(f"Ingrese el nombre del producto {i+1}: ")
    precio = float(input(f"Ingrese el precio de '{nombre}': "))
    productos.append(nombre)
    precios.append(precio)

total = sum(precios)

indice_max = precios.index(max(precios))
indice_min = precios.index(min(precios))

producto_mas_caro = productos[indice_max]
producto_mas_barato = productos[indice_min]

print("--- RESULTADOS ---")
print(f"Precio total de todos los productos: ${total:.2f}")
print(f"Producto más caro: {producto_mas_caro} (${max(precios):.2f})")
print(f"Producto más barato: {producto_mas_barato} (${min(precios):.2f})")