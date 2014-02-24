#!/usr/bin/python
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
print 
if ((mitad % 2) == 1):
print "\n"

