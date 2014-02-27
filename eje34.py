#!/usr/bin/python
#!encoding: UTF-8
from math import *


#Explicacion del primer apartado
# a) if ( (x != 0.0) and ( (z - x) / x * x < 2.0)):
x = 5.0
z = 10.0
print z - x 
print x * x
print (z - x) / (x * x)
if ( (x != 0.0) and (((z - x) / (x * x)) < 2.0)):
	print "Entra en el if"
print "\n"

#Explicacion del primer apartado
# b) if (( (z - x) / x * x < 2.0) and (x != 0.0)):
x = 5.0
z = 10.0
print z - x 
print x * x
print (z - x) / (x * x)
if ((((z - x) / (x * x)) < 2.0) and (x != 0.0)):
	print "Entra en el siguiente if"
print "\n"

#Explicacion del tercer apartado
# c) if a == 0 or 1/a > 1:
a = 0.1
if (a == 0) or (a < 1):
	print "Entra en el tercer if"
print "\n"

#Explicacion del cuarto apartado
# d) if a != 0 and 1/a > 1:
a = 0.2
if (a != 0) and (a < 1):
	print "Entra en el cuarto if"
print "\n"

#Explicacion del quinto apartado
# e) if 1/a > 1 and a != 0:
a = 0.2
if (a < 1) and (a != 0):
	print "Entra en el quinto if"
print "\n"


