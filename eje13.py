#!/usr/bin/python
from math import *

print "Introduzca el primer lado de un triangulo: "
a = float (raw_input());
print "Introduzca el segundo lado de un triangulo: "
b = float (raw_input());
print "Introduzca el tercer lado de un triangulo: "
c = float (raw_input());

p = (a + b + c) / 2;
area = sqrt (p * (p - a)*(p - b)*(p -c));
print "El perimetro del triangulo con lados", a, b, c, "es", p 
print "El area del triangulo con lados", a, b, c, "es", area
print "\n"

