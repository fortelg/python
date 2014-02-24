#!/usr/bin/python
from math import *

print "Introduzca el valor del producto: "
precio = float (raw_input());

pvp  = precio + (precio * (21.0 / 100.0));
print "El valor total del precio %.2f es %.2f" % (precio, pvp)
print "\n"

