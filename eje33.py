#!/usr/bin/python
#!encoding: UTF-8
from math import *

print "Introduzca la coordenada en x para el punto inicial:"
punto_inicial_x = int (raw_input());
print "Introduzca la coordenada en y para el punto inicial:"
punto_inicial_y = int (raw_input());

vector = [];
for i in range(4):
	print "Introduzca las coordenadas para el punto", i, ":"
	vector.append([]);
	for j in range(2):
		print "Coordenada", j, ":"
		dato = int (raw_input());
		vector[i].append(dato);

distancia = [];
for i in range(4):
	d = sqrt (((punto_inicial_x - vector[i][0])**2) + ((punto_inicial_y - vector[i][1])**2));
	distancia.append(d);

menor = distancia[0];
pos = 0;
for i in range(1,4):
	if (distancia[i] < menor):
		menor = distancia[i];
		pos = i;
print "El punto con menor distancia al primero es", vector[pos][0], vector[pos][1] 
print "\n"

