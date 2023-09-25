import numpy as np
import random
from fractions import Fraction

print("hola mundo")
variableTexto = "hola soy un texto"
print(variableTexto)
print(4 + 7)
print(Fraction(5, 12))
# division entera
print(5 // 4)

manzanas = 50

niños = 6

cantidad_de_manzanas_por_niño = manzanas // niños

print(cantidad_de_manzanas_por_niño)

# float
soyunFloat = 8.9
# string
soyString = "oli"

# precioDolar = int(input("Ingresa el precio del dolar:\n"))
# cantidaddedolares = int(input("ingresa la cantidad de dolares por cambiar: \n"))
# cantidad_en_pesos = precioDolar * cantidaddedolares
# print(cantidad_en_pesos)

nombre = print("ingresa nombre")

a = 1
a = 1
b = 2
a = a + 1
a = a * 10
b = a // 3
c = b % 2
print("valor de C")
print(c)

# dias_vacaciones = "10.2"
# cant_dinero = dias_vacaciones /2
# print(cant_dinero)

print(9 != 9)

cantidad_de_manzanas_por_niño

if not True:
    print("soy true")
else:
    print("soy else")

numero_dado = random.randint(1, 6)
print("El numero del dado es " + str(numero_dado))

# if elif else

# if
# elif
# elif
# else

numero_dado = random.randint(1, 6)
print("El numero del dado es " + str(numero_dado))

if numero_dado == 1:
    print("fuiste asignado a grupo 1")
elif numero_dado == 2:
    print("fuiste asignado a grupo 2")
elif numero_dado == 3:
    print("fuiste asignado a grupo 3")
else:
    print("quedaste sin grupo")

# while True:
#    print("hola")

while False:
    print("chao")

variable_numerica = 1
while variable_numerica <= 20:
    print(str(variable_numerica))
    variable_numerica = variable_numerica + 1
    break

print("termino el conteo")

# comando for

for i in range(1, 20):
    print(i)

for i in range(5, 10):
    print(i)

i = 5
while i <= 10:
    print(i)
    i = i + 1

variable_boolean = True


def nombre_fx(a, b, c):
    # ejecucion del codigo
    return a + b + c

def Sumar(a, b):
    return Fraction(a + b)

print(Sumar(45,5.5))

texto1 = "olis"
texto2 = "bye"

print(texto1+texto2)

#primera letra de un string
saludo = "hola"

primera_letra = texto1[0]
print(primera_letra)

#funcion len

soyUntexto = "ola que tal"

print(len(soyUntexto))

#slice para extraer un rango

string_de_ejemplo = "texto de ejemplo"
primera_palabra = string_de_ejemplo[0:5]
print(primera_palabra)
segunda_palabra = string_de_ejemplo[5:8]
print(segunda_palabra)

#imprimir todos los caracteres
#usar un for
s = "ejemplo"
for caracter in s:
    print(caracter)
#comparacion de string

variable1 = "a"
variable2 = "b"

print(variable1 == variable2)

#funcion count
s = "papapapepa"
print (s.count("a"))

print (s.find("pe"))
print(s.replace("pa","xx"))

#todo a mayusculas
print(s.upper())
print(s.lower())

#strip remueve espacios y otros caracteres
print("\npalabra con cosas                 ".strip())

mylist = ["apple", "banana", "cherry"]

for fruta in mylist:
    print(fruta)

#elemento = 0
#cantidad_productos = 3
#while elemento <= cantidad_productos:
#    print(mylist[elemento])
#    elemento = elemento + 1

#listas de listas , van del 0 al 2
matriz = [["a", "b", "c"], ["d", "e", "f"], ["g", "h", "i"]]
#M[i][j] para acceder a la posicion

print(matriz[0][0])

matriz[2][1] = "z"
print(matriz[2][1])

#para saber el numero de filas
print(len(matriz))
#numero de columnas
print(len(matriz[0]))

informacion_archivo = open("ejemplo1.txt", "a", encoding="UTF-8")
#lineas = informacion_archivo.readlines() #genera una lista
#for linea in lineas:
#    print(linea)

informacion_archivo.write("mi nombre es rodrigo")
informacion_archivo.close()

informacion_archivo = open("ejemplo1.txt", "w", encoding="UTF-8") #w sobreescribe todo
informacion_archivo.write("mi nombre es pedrito")
informacion_archivo.close()

#ejemplo abriendo archivos csv
archivo = open("ejemplo1.csv", "r", encoding="UTF-8")
lineas = archivo.readlines()
archivo.close()

numero_clientes = len(lineas)
matriz_de_datos = []
for linea in lineas:
    linea = linea.strip()
    fila = linea.split(";")
    matriz_de_datos.append(fila)
print(matriz_de_datos)

for fila in matriz_de_datos:
    valor_tipo_cliente = fila[4]
    #fila[4] = fila[4].replace("-.!#", "")
    #fila[4] = fila[4].strip("-.!#")
    fila[4] = fila[4].lstrip("-.!#")
    fila[4] = valor_tipo_cliente[len(valor_tipo_cliente)-1]

#para calcular la edad
for fila in matriz_de_datos:
    fecha_nacimiento = fila[3]
    fecha_nacimiento_lista = fecha_nacimiento.split("/")
    edad = 2023 - int(fecha_nacimiento_lista[0])
    fila.append(edad)

print(matriz_de_datos)

archivo_guardar = open("ejemplo_con_edad.csv","w")
for fila in matriz_de_datos:
	fila_para_escribir = ""

	for i in range(0,len(fila)):
		if i == len(fila)-1:
			fila_para_escribir += str(fila[i])
		else:
			fila_para_escribir += fila[i] + ";"

	fila_para_escribir += "\n"

	archivo_guardar.write(fila_para_escribir)

archivo_guardar.close()
