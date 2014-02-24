#!/usr/bin/python
#!encoding: UTF-8
from math import *

print "Introduzca el año: "
anio = int (raw_input());

if (((anio % 4) == 0) and ((anio % 100) == 1)) or ((anio % 400) == 0):
	print "Bisiesto"
else:
	print "No es Bisiesto"
print "\n"

if (((anio % 4) == 0) and ((anio % 100) == 1)):
	print "Bisiesto";
elif ((anio % 400) == 0):
	print "Bisiesto"
else:
	print "No es Bisiesto"
print "\n"

if ((anio % 4) == 0):
	if ((anio % 100) == 1):
		print "Bisiesto";
if ((anio % 400) == 0):
	print "Bisiesto"
else:
	print "No es Bisiesto"
print "\n"
