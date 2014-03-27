#!/usr/bin/python
#!encoding: UTF-8

def buscar (cadena1, cadena2):
	resultado = []
	for i in cadena1:
		encontrado = 0
		for j in resultado:
			if (i == j):
				encontrado = 1
		if (encontrado == 0):
			resultado.append(i)
	for i in cadena2:
		encontrado = 0
		for j in resultado:
			if (i == j):
				encontrado = 1
		if (encontrado == 0):
			resultado.append(i)
	return (resultado)


print "Introduzca el tamaño de la lista a introducir:"
n = int (raw_input())
lista = []
for i in range (n):
	print "Introduzca el elemento", i, ":"
	dato = int (raw_input())
	lista.append(dato)
print "Introduzca el tamaño de la siguiente lista a introducir:"
n = int (raw_input())
lista2 = []
for i in range (n):
	print "Introduzca el elemento", i, ":"
	dato = int (raw_input())
	lista2.append(dato)

otra = buscar (lista, lista2)
print "La lista resultante es"
print otra
print "\n"
