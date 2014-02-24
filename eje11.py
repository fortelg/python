#!/usr/bin/python
from math import *

print "Introduzca el radio de un cilindro: "
radio = float (raw_input());
print "Introduzca la altura de un cilindro: "
altura = float (raw_input());

area = 2 * pi * radio;
volumen = area * altura;

print "El area del cilindro con radio", radio, "es", area
print "El volumen del cilindro con radio", radio, "es", volumen 
print "\n"

