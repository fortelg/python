#!/usr/bin/python
#!encoding: UTF-8

print "Introduzca el valor para n:"
n = int (raw_input())
print "Introduzca el valor para m:"
m = int (raw_input())


numeros = []
for i in range(n, m+1):
	numeros.append(i)
print "Los numeros almacenados son:"
for i in range(m-n+1):
	print numeros[i]
suma = 0
for i in range(m-n+1):
	suma += numeros[i]
print "La suma de los numeros es", suma

#Otra forma de hacerlo
suma = 0
for i in range(n, m+1):
	suma += i
print "La suma de los numeros es", suma

print "\n"

