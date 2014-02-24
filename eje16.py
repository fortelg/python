#!/usr/bin/python
from math import *

print "Introduzca el valor de a: "
a = float (raw_input());
print "Introduzca el valor de b: "
b = float (raw_input());
print "Introduzca el valor de c: "
c = float (raw_input());

x1  = (-b + sqrt (b * b - 4 * a * c)) / (2 * a);
x2  = (-b - sqrt (b * b - 4 * a * c)) / (2 * a);
print "Los valores de de la ecuacion de segundo grado x1 es %.2f y x2 es %.2f" % (x1, x2)
print "\n"

