# len()
# eval()
# zip()
# truthy y falsy
# control de flujo Condicional IF
# ternario

# operador = "*"
# n1 = "2"
# n2 = "3"
#
# resultado = eval(n1 + operador + n2)
# print(f'el resultado es:  {resultado}')
#
# print('*****')
#
# lista1 = ['a', 'b', 'c']
# lista2 = [1, 2, 3]
# lista_de_tuplas = list(zip(lista1, lista2))False
# print("Lista de tuplas combinadas:", lista_de_tuplas)
#
#
#
# lista = []
# esta_vacia = not bool(lista)
# print(esta_vacia)
# if esta_vacia:
#     print("La lista está vacía.")
# else:
#     print("La lista no está vacía.")
#

"""
Escribe un programa que ayude a calcular el gasto y el consumo de gaseosas de un individuo en un período determinado. El usuario proporcionará la cantidad de latas de gaseosa que consume semanalmente. Utilizando esta información, el programa calculará el gasto total en gaseosas en un año y determinará si el nivel de consumo es alto o medio, basado en ciertos criterios predefinidos.

El precio promedio de una lata de gaseosa es de $1500. El programa clasificará el nivel de consumo como "alto" si la cantidad total de latas consumidas en tres años es mayor a 600 y el gasto total en gaseosas supera los $900.000.
 si consumo entre 300 y 600 y valor entre 400.000 y 900.000 sera medio
 En caso contrario, se clasificará como "bajo".
"""

# Solicitar al usuario la cantidad de latas de gaseosa que consume semanalmente
# latas_semana = int(input("¿Cuántas latas de gaseosa consumes semanalmente?: "))
#
# # Calcular el precio promedio de una lata de gaseosa
# precio_lata = 1500
#
# # Calcular la cantidad de latas de gaseosa consumidas en un año
# latas_anio = latas_semana * 52
#
# # Calcular el gasto total en gaseosas en un año
# gasto_total = precio_lata * latas_anio

# Imprimir la cantidad total de latas de gaseosa consumidas en tres años y el gasto total en gaseosas
# print("Cantidad total de latas de gaseosa consumidas en tres años:", latas_anio * 3)
# print("Gasto total en gaseosas:", gasto_total * 3)
#
# # Determinar si el nivel de consumo es alto o medio
# if (latas_anio * 3) > 600 and (gasto_total*3) > 900000:
#     print("Tu nivel de consumo de gaseosas es alto.")
# elif (latas_anio * 3) > 300 and (gasto_total*3) > 400000:
#     print("Tu nivel de consumo de gaseosas es medio.")
# else:
#     print("Tu nivel de consumo de gaseosas es bajo")
#
#
# cadena = "Pan".capitalize()
#
# print(cadena)

# Ejemplo de uso de truhy y falsy en una declaración if
valor = 10
if valor:
    print("El valor es truhy")
else:
    print("El valor es falsy")

""""""

# Dada una tupla y un elemento, encuentra su índice en la tupla preguntale al usuario el valor a consultar

tupla = (10, 20, 30, 40, 50)
elemento = 30
indice = tupla.index(elemento)
print("El índice del elemento", elemento, "es:", indice)

""""""

# lista = []
# tarea1 = input('Ingresa una tarea')
# lista.append(tarea1)
# print(f'tienes {len(lista)} tareas')
# tarea2 = input('Ingresa una tarea')
# lista.append(tarea2)
# print(f'tienes {len(lista)} tareas')
# tarea3 = input('Ingresa una tarea')
# lista.append(tarea3)
# print(f'tienes {len(lista)} tareas')
# tarea4 = input('Ingresa una tarea')
# lista.append(tarea4)
# print(f'tienes {len(lista)} tareas')
# tarea5 = input('Ingresa una tarea')
# lista.append(tarea5)
# print(f'tienes {len(lista)} tareas')
#
# print(lista)

""""""
# TEMA
# import sys   sys.exit()

#slicing
#palabra = 'reconocet'
#print(palabra[::-1])

# TEMA if anidado
miVariable = 'framework'
variableAnidada = 'Python'

if miVariable == 'lenguaje':
    if variableAnidada == 'Python':
        print(f"El lenguaje es {variableAnidada}")
    else:
        print('NO CORRESPONDE')
elif miVariable == 'framework':
    if variableAnidada == 'Django':
        print(f"El framework es {variableAnidada}")
    else:
        print('NO CORRESPONDE')

# import sys
#
# print("Seleccione un departamento")
# departamento = int(input('1. Cundinamarca\n2. Valle\n3. Antioquia\n==> '))
# if departamento == 1:
#     departamento = 'Cundinamarca'
# elif departamento == 2:
#     departamento = 'Valle'
# elif departamento == 3:
#     departamento = 'Antioquia'
# else:
#     print('No ingresaste una opcion valida')
#     sys.exit()
#
# print("Seleccione un municipio")
# municipio = int(
#     input('1. Yumbo\n2. Chia\n3. Envigado\n4. Palmira\n5. Madrid\n6. Guatape\n7. Bello\n8. Buga\n9. Tocancipa\n==> '))
# if municipio == 1:
#     municipio = 'Yumbo'
# elif municipio == 2:
#     municipio = 'Chia'
# elif municipio == 3:
#     municipio = 'Envigado'
# elif municipio == 4:
#     municipio = 'Palmira'
# elif municipio == 5:
#     municipio = 'Madrid'
# elif municipio == 6:
#     municipio = 'Guatape'
# elif municipio == 7:
#     municipio = 'Bello'
# elif municipio == 8:
#     municipio = 'Buga'
# elif municipio == 9:
#     municipio = 'Tocancipa'
# else:
#     print('No ingresaste una opcion valida')
#     sys.exit()
#
# cundinamarca = ['Chia', 'Madrid', 'Tocancipa']
# valle = ['Palmira', 'Yumbo', 'Buga']
# antioquia = ['Envigado', 'Guatape', 'Bello']
#
# if departamento == 'Cundinamarca':
#     print(f'{municipio} es un municipio de {departamento}') if municipio in cundinamarca else print(f'{municipio} no es un municipio de {departamento}')
# elif departamento == 'Valle':
#     print(f'{municipio} es un municipio de {departamento}') if municipio in valle else print(f'{municipio} no es un municipio de {departamento}')
# elif departamento == 'Antioquia':
#     print(f'{municipio} es un municipio de {departamento}') if municipio in antioquia else print(f'{municipio} no es un municipio de {departamento}')
#

# mi_diccionario = {'nombre': 'Juan', 'edad': 30, 'ciudad': 'Madrid'}
# print(mi_diccionario)


