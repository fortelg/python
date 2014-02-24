#!/usr/bin/python
from math import *

print "Introduzca la cantidad de preguntas realizadas: "
realizadas = float (raw_input());
print "Introduzca la cantidad de preguntas correctas: "
correctas = float (raw_input());

porcentaje = (correctas / realizadas) * 100.0;
print "El porcentaje obtenido es ", porcentaje

if (porcentaje >= 90.0):
	print "Muy bueno"
elif (porcentaje >= 70.0):
	print "Bueno"
elif (porcentaje >= 50.0):
	print "Regular"
else:
	print "Malo"
print "\n"

