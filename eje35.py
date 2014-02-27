#!/usr/bin/python
#!encoding: UTF-8

#Para la primera combinación
for i in range(1,4):
	if (i == 1):
		print "El valor de i es", i
		print "y ejecuto la sentencia stmt1"
	elif (i == 2):
		print "El valor de i es", i
		print "y ejecuto la sentencia stmt2"
	elif (i == 3):
		print "El valor de i es", i
		print "y ejecuto la sentencia stmt3"
print "\n"

#Para la segunda combinación
for i in range(1,4):
	if (i == 1):
		print "El valor de i es", i
		print "y ejecuto la sentencia stmt2"
	elif (i == 2):
		print "El valor de i es", i
		print "y ejecuto la sentencia stmt1"
		print "y ejecuto la sentencia stmt3"
	elif (i == 3):
		print "El valor de i es", i
		print "y ejecuto la sentencia stmt1"
print "\n"

#Para la tercera combinación
for i in range(1,4):
	if (i == 1):
		print "El valor de i es", i
		print "y ejecuto la sentencia stmt1"
		print "y ejecuto la sentencia stmt2"
	elif (i == 2):
		print "El valor de i es", i
		print "y ejecuto la sentencia stmt1"
		print "y ejecuto la sentencia stmt2"
	elif (i == 3):
		print "El valor de i es", i
		print "y ejecuto la sentencia stmt2"
		print "y ejecuto la sentencia stmt3"
print "\n"

