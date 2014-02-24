#!/usr/bin/python
from math import *

print "Introduzca la nota numerica: "
nota = float (raw_input());

if (nota >= 9.0):
	print "Sobresaliente"
elif (nota >= 7.0):
	print "Notable"
elif (nota >= 5.0):
	print "Aprobado"
else:
	print "Suspenso"
print "\n"

