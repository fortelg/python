#!/usr/bin/python
#!encoding: UTF-8
from math import *

print "Introduzca la cantidad de dias: "
total_dias = int (raw_input())
dias = total_dias

anios = dias / 365
dias = dias % 365
meses = dias / 30
dias = dias % 30
semanas = dias / 7
dias = dias % 7

print "La conversión de", total_dias,"a años, meses, semanas y dias es:"
if (anios != 0):
	print anios, "años" 
if (meses != 0):
	print meses, "meses" 
if (semanas != 0):
	print semanas, "semanas" 
if (dias != 0):
	print dias, "dias" 
print "\n"

