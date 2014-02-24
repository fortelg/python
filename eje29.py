#!/usr/bin/python
#!encoding: UTF-8
from math import *

print "Introduzca la cantidad de euros: "
euros = int (raw_input());

bil500 = euros / 500;
euros = euros % 500;
bil200 = euros / 200;
euros = euros % 200;
bil100 = euros / 100;
euros = euros % 100;
bil50 = euros / 50;
euros = euros % 50;
bil20 = euros / 20;
euros = euros % 20;
bil10 = euros / 10;
euros = euros % 10;
bil5 = euros / 5;
euros = euros % 5;
mon2 = euros / 2;
euros = euros % 2;
mon1 = euros;

print "La conversión a billetes y monedas son:"
if (bil500 != 0):
	print bil500, "billetes de 500€" 
if (bil200 != 0):
	print bil200, "billetes de 200€" 
if (bil100 != 0):
	print bil100, "billetes de 100€" 
if (bil500 != 0):
	print bil50, "billetes de 50€" 
if (bil20 != 0):
	print bil20, "billetes de 20€" 
if (bil10 != 0):
	print bil10, "billetes de 10€" 
if (bil5 != 0):
	print bil5, "billetes de 5€" 
if (mon2 != 0):
	print mon2, "monedas de 2€" 
if (mon1 != 0):
	print mon1, "monedas de 1€" 
print "\n"

