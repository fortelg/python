#!/usr/bin/python
#!encoding: UTF-8
from math import *

vector = [];
for i in range(5):
	print "Introduzca una palabra: "
	palabra = raw_input();
	vector.append(palabra);

menor = vector[0];
for i in range(1,5):
	if (vector[i] < menor):
		menor = vector[i];
print "La cadena mas pequeña es", menor 



#Otra forma de ordenar las palabras

vector.sort();
print "La cadena mas pequeña es",vector[0] 

print "\n"

