#!/usr/bin/python
from math import *

print "Introduzca la cantidad de euros: "
euros = float (raw_input());
print "Introduzca la tasa de interes: "
tasa = float (raw_input());
print "Introduzca el n de anios: "
anios = float (raw_input());

interes = euros * ((tasa / 100.0) * anios);
capital = euros + interes
print "El valor total del capital interes es %.2f capital es %.2f " % (interes, capital)
print "\n"

