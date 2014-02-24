#!/usr/bin/python
from math import *

print "Introduzca la base de un triangulo: "
base = float (raw_input());
print "Introduzca la altura de un triangulo: "
altura = float (raw_input());

hipotenusa = sqrt (base * base + altura * altura);
print "La hipotenusa del triangulo con base", base, "y altura", altura, "es %.2f" % hipotenusa
print "\n"

