#!/usr/bin/python
from math import *

print "Introduzca la primera edad: "
edad1 = int (raw_input());
print "Introduzca la segunda edad: "
edad2 = int (raw_input());

if (edad1 < edad2):
	print "La primera edad es menor"
elif (edad2 < edad1):
	print "La segunda edad es menor"
else:
	print "Las edades son iguales"
print "\n"

