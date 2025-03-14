# El ciclo while en Python se utiliza para ejecutar un bloque de código repetidamente siempre que una condición especificada sea verdadera. Su estructura básica es:

# La condición se evalúa antes de cada iteración. Si la condición es verdadera, el bloque de código dentro del while se ejecutará; si la condición es falsa, el ciclo while se detendrá y la ejecución del programa continuará después del bloque while.

while condición:
    #CODIGO A EJECUTAR

contador = 1
while contador <= 5:
    print(contador)
    contador += 1
print('******************************')

numeros = [1, 3, 5, 7, 9, 11]
indice = 0
while indice < len(numeros):
    print(numeros[indice])
    indice += 1

# Ejemplo 1: Suma de números hasta cierto límite
suma = 0
numero = 1
limite = 10
while numero <= limite:
    suma += numero
    numero += 1
print("La suma de los números del 1 al", limite, "es:", suma)

# Ejemplo 2: Validación de entrada del usuario
respuesta = ""
while respuesta.lower() != "sí":
    respuesta = input("¿Quieres continuar? (Sí/No): ")
print("¡Bien! Has confirmado que quieres continuar.")

# ESTUDIANTE Ejercicio: Juego de adivinanza
import random

numero_secreto = random.randint(1, 100)
intentos = 0
adivinanza = 0

print("Adivina el número secreto entre 1 y 100.")

while adivinanza != numero_secreto:
    adivinanza = int(input("Introduce tu adivinanza: "))
    intentos += 1

    if adivinanza < numero_secreto:
        print("El número secreto es más grande.")
    elif adivinanza > numero_secreto:
        print("El número secreto es más pequeño.")

print("¡Felicidades! ¡Adivinaste el número en", intentos, "intentos!")

#ESTUDIANTE Ejercicio: Iteración hasta que se cumpla una condición específica
cartas_en_mano = []
while len(cartas_en_mano) < 5:
    nueva_carta = input("Toma una nueva carta: ")
    cartas_en_mano.append(nueva_carta)
print("Tienes un total de 5 cartas en tu mano:", cartas_en_mano)

# El ciclo for en Python se utiliza para iterar sobre una secuencia (como una lista, una tupla, un diccionario, etc.) y ejecutar un bloque de código una vez para cada elemento de la secuencia. Su estructura básica es

for i in secuencia:
    # Código a ejecutar

# Ejemplo # 1: Iterar sobre una lista
frutas = ["manzana", "banana", "cereza"]
for fruta in frutas:
    print(fruta)

#Ejemplo 2: Iterar sobre una cadena de texto
mensaje = "Hola mundo"
for caracter in mensaje:
    print(caracter)

#Ejemplo 3: Iterar sobre un rango de números
for i in range(5):
    print(i)

# RANGE es una función incorporada que se utiliza para generar una secuencia de números enteros.
range(inicio, fin, paso)
# El inicio es opcional y empieza por defecto en 0
# El fin es obligatorio y no va incluido

numeros = list(range(5))
print(numeros)

#ESTUDIANTE Ejercicio:
for i in range(2,20,2):
    print(i)

#Ejemplo 5: Iterar sobre una lista de tuplas
puntos = [(1, 2), (3, 4), (5, 6)]
for punto in puntos:
    x, y = punto
    print("x:", x, ", y:", y)

#Ejemplo 6: Uso de enumerate para obtener índices y elementos

colores = ["rojo", "verde", "azul"]
for indice, color in enumerate(colores):
    print("El color en la posición", indice, "es", color)




