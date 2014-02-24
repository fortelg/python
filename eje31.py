#!/usr/bin/python
#!encoding: UTF-8
from math import *

vector = [];
for i in range(5):
	print "Introduzca un numero: "
	num = int (raw_input());
	vector.append(num);

maximo = vector[0];
for i in range(1,5):
	if (vector[i] > maximo):
		maximo = vector[i];

print "El numero máximo introducido es", maximo 
print "\n"

