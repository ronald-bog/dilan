# tipos primitivos
# Strings = str
# Enteros = int
# Flotantes = float
# Complejos 
# Booleanos = bool
# Valores = None

# Declarar,
# Asignar,
# Inicializar



miVariable = None

nombreUniversidad = "Nacional"

# Enteros = int Integer
miNumero = 1001
notaParcial = 50
cantidadPrendas = 6
cantidadHermanos = 3
materias_inscritas = 5
cantidad_electivas = 2

# Tipo String
nombreAlumno = "DILAN"
nombreProfe = "Ronald"
primerMateria = "Cálculo"
nombre_hermano = "SAMUEL"
facultad_estudiante = "Ingeniería Electrónica"
carrera_estudiante = "***684646416***"
ejemplo = "Bienvenido al curso de Python"



# Tipo float
numeroDecimal = 3.14
euler = 2.71
promedio_estudiante = 3.8
estaturaAlumno = 1.72
longitud_cuaderno = 15.67
velocidadPromedio = 1.74

# Tipo Booleano True False
correcto = True
asignaturaAprobada = False
asistencia = True

validacion = type(asistencia)

# print(facultad_estudiante.replace("Electrónica", "Sistemas"))
# print(ejemplo.replace("Python", "Java"))

print(facultad_estudiante[0])

# valido="de" in ejemplo
print(type(miNumero.__str__()))

print(cantidadPrendas * cantidadHermanos)

# print(miNumero)
# print(notaParcial)
# print(cantidadPrendas)
# print(cantidadHermanos)
# print(materias_inscritas)
# print(cantidad_electivas)
# print(nombreAlumno)
# print(nombreProfe)
# print(primerMateria)
# print(nombre_hermano)
# print(facultad_estudiante)
# print(carrera_estudiante)
# print(numeroDecimal)
# print(euler)
# print(promedio_estudiante)
# print(estaturaAlumno)
# print(longitud_cuaderno)
# print(velocidadPromedio)
# print(correcto)
# print(asignaturaAprobada)
# print(asistencia)

"""
#Operadores Aritmeticos + - * / % ** //

Operadores de comparacion: == != > < => =<

Operadores de Asignacion
Asignacion =
suma y Asignacion +=      x = x + 5       x += 5
resta y asignacion -= 
multiplica y asigna *=
divina y asigna /=

Operadores Logicos:
AND (and) xxxxx AND yyyyyy 
OR (or)     1expresion OR 2expresion 
NOT (not)

Operadores Pertenencia: in  /   not in
Operadores de identidad:
is: a is b 
is not

dame un 'valor':

"""
a = 48
b = 6 * 8
print(a == b)

# entrada = input('dame un valor')

# print(entrada + 1000)
# print(f'el valor {entrada} que me diste es: {entrada}')

# nombre = input("dame tu nombre: ")
# apellido = input("dampe tu apellido: ")
# edad  = input("dame tu edad: ")
# print(f"Tu nombre es {nombre},\ntu apellido {apellido},\ny tu edad {edad}")

operacion = input("Operación a realizar: ")
numero1 = int(input("Ingrese un primer número: "))
numero2 = int(input("Ingrese un segundo número: "))
print(f"La operación entre {numero1} / {numero2} es igual a {numero1 // numero2}")
