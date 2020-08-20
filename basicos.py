print("Hola mundo!")
print("Adiós mundo!")
#operaciones
print(4+6)
print(5-2)
print(3*4)
print(20/4)
#precedencia de operadores
print(5+8*(3+2))

#Tipos de datos
print(type(2))
print(type(8.62))
print(type("textoo"))
print(type('aaaa'))
print(type("8"))

#Variables
mensaje = "Esto es un mensaje"
print(mensaje)
mensaje ="se modifico xde"
print(mensaje)
print (type(mensaje))
mensaje = 100
print(mensaje)
print (type(mensaje))

mis3animales = "Perico, gallo, chivo"
print(mis3animales)

tresAnimales = "Perico, gallo, chivo"
print (tresAnimales)
textoUno = "Mi texto"
textoDos = "Mi 2 texto"
print(textoUno + textoDos)
edad = 20
print("La edad del usuario es: " + str(edad))
print("La tipo de dato de edad es: " + str(type(edad)))

import math
grados = 45.0
radianes = grados * math.pi / 180.0
seno = math.sin(radianes)
print("Seno de 45° : " + str(seno))

def saludar(nombre):
    print("Hola " + nombre)
    print("Que rollo?")
    print("aqui nomas")
def despedir():
    print("Sale pues al rato")
    print("Ay nos vidrios")
def concatenar(parte1, parte2):
    return parte1 + parte2

print("Esto no es parte de la función")
saludar("Rubén")
despedir()

frase = concatenar("Hola ", "Adios")
print(frase)