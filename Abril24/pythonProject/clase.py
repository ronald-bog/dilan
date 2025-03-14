# myString = 'SOL'
# miLista = ('Python','Java','JS')
# a, b, c = miLista
# print(a)
# print(b)
# print(c)

# While
# while condicion:
# Logica que queremos que haga en cada iteracion
# contador = 1
# while contador <= 5:
#     print(contador)
#     contador += 1
# numbers = [5, 6, 90, 2, 5]
# indice = 0
# while indice < len(numbers):
#     print(numbers[indice])
#     indice += 1

# num = 1
# total = 5
# suma = 0
# while num <= total:
#     suma += num
#     num += 1
#
# print(suma)

# respuesta = ''
# while respuesta.lower() == 'si':
#     respuesta = input("Quieres continuar? (Si - No)")
#
# print("Finalizando programa")

# FOR
#for i in secuencia:
    #Codigo a Ejecutar en cada iteracion

# frutas = ['sandia','fresa','mango']
# saludo = 'Hola Mundo'
# for letra in saludo:
#     print(letra)
#range(inicio, fin, paso)

# for i in range(5):
#     print(i)

coord = [(1,2),(3,4),(5,6)]
for j in coord:
    x, y = j
    print('x = ', x, 'y = ', y )

colores = ['red', 'green', 'blue']
for indice, valor in enumerate(colores):
    print(f"El valor en la posicion {indice} es {valor}")