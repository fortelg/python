#!/usr/bin/python
from math import *

print "Introduzca la base de un triangulo: "
base = float (raw_input());
print "Introduzca la altura de un triangulo: "
altura = float (raw_input());

area = (base * altura) / 2;
hipotenusa = sqrt (base * base + altura * altura);
perimetro = base + altura + hipotenusa;
print "El area del triangulo con base", base, "y altura", altura, "es", area
print "El perimetro del triangulo con base", base, "y altura", altura, "es", perimetro
print "\n"

