#!/usr/bin/python

a = "luis "
b = a * 1000
print "El valor inicial era:", a
print "El valor final es:", b
print "\n"


#Haciendo uso de bucles

a = "luis "
b = a
for i in range(1000):
	b = b + a
print b

