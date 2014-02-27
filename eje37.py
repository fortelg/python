#!/usr/bin/python
#!encoding: UTF-8


numeros = []
for i in range(1, 11):
	numeros.append(i)
print "Los numeros almacenados son:"
for i in range(10):
	print numeros[i]
suma = 0
for i in range(10):
	suma += numeros[i]
print "La suma de los numeros es", suma

#Otra forma de hacerlo
suma = 0
for i in range(1, 11):
	suma += i
print "La suma de los numeros es", suma

print "\n"

