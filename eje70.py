#!/usr/bin/python
#!encoding: UTF-8

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

otra = []
for i in lista2:
	for j in lista:
		if (i == j):
			otra.append(j)

print otra
