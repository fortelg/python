#!/usr/bin/python
#!encoding: UTF-8

#Para la primera combinación
print "Introduzca el numero de calificaciones a realizar:"
num = int (raw_input())

notas = []
for i in range(num):
	print "Introduzca la nota ", i, ":"
	nota = float (raw_input())
	notas.append(nota)
print "Las notas introducidas son:"
for i in range(num):
	print notas[i]

suma = 0.0
for i in range(num):
	suma += notas[i]
media = suma / num;
print "La media aritmética es", media

print "\n"

