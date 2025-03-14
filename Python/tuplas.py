miTupla = (1, 2, 3, 4, 5, 6)
print(miTupla)

arreglo =  {"nombre": "Juan", "edad": 30, "ciudad": "Madrid"}
print(arreglo)
a, b, c = arreglo

print(a)
print(b)
print(c)

colores = ["rojo", "verde", "azul"]
for indice, color in enumerate(colores):
    print("El color en la posición", indice, "es", color)