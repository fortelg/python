#!/usr/bin/python
#!encoding: UTF-8
from math import *

print "Introduzca un numero: "
num = int (raw_input());

primo = 1;
for i in range(2,(num-1)):
	if ((num % 2) == 0):
		primo = 0;

if (primo):
	print "El numero introducido es primo" 
else:
	print "El numero introducido no primo" 
print "\n"

