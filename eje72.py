#!/usr/bin/python
#!encoding: UTF-8

def buscar (nombres, caracter):
	resultado = []
	for i in nombres:
		if (i[0] == caracter):
			resultado.append(i)
	return (resultado)


print "Introduzca el tamaño de la lista a introducir:"
n = int (raw_input())
lista = []
for i in range (n):
	print "Introduzca el", i, "nombre:"
	dato = raw_input()
	lista.append(dato)
print "Introduzca el caracter a buscar:"
caracter = raw_input()
otra = buscar (lista, caracter)
print "La lista resultante es"
print otra
print "\n"


#Si realmente queremos controlar que sólo se pulse una tecla en el campo del caracter,
#tal como esta ahora, no podemos ya que tenemos el rwa_input, y esto puede almacenar
#una cadena de caracteres. Lo podemos solucionar preguntando por la longitud de dicha variable,
#si es mayor que 1, ya sabemos que han pulsado mas de un caracter y nos quedaríamos con caracter[0]
#
#
#Otra forma de leer un caracter por teclado es mediante el paquete getch
#Para ello debemos de tenerlo instalado
#      #import getch
#
#      print "Introduzca el caracter a buscar:"
#      caracter = getch.getch()
#
#
# Si usamos la funcion getch.getch(), al pulsar una tecla, dicho caracter se almacena
# en la variable caracter. Podemos hacer uso de la funcion
#
#      print "Introduzca el caracter a buscar:"
#      caracter = getch.getche()
#
# Si usamos la funcion getch.getche(), al pulsar una tecla, dicho caracter se visualiza por
# pantalla y también se almacena en la variable caracter.
#

