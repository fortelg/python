#!/usr/bin/python

print "Introduzca un numero: "
a = int (raw_input());

print "Introduzca otro numero: "
b = int (raw_input());

tmp = a
a = b
b = tmp

print "El valor de la primera variable es", a, "y el de la segunda es", b
print "\n"

