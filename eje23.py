#!/usr/bin/python
#!encoding: UTF-8
from math import *

h = float (raw_input('Dame h: '));
v = float (raw_input('y v: '));
z = h * v;

print "Resultado 1 %6.2f"%z
v = 2*h + v+v;
print 'Resultado 2 %6.2f'%v
print "\n"

#Mas legible
print "Introduzca un valor para h:"
h = float (raw_input());
print "Introduzca un valor para v:"
v = float (raw_input());
z = h * v;
print "El primero resultado es %6.2f" % z
z = 2 * (h + v);
print "El segundo resultado es %6.2f" % z
print "\n"

