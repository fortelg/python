#!usr/bin/python
#!encoding: UTF-8


def esprimo (n):
	primo = 1
	if (n > 2):
		for i in range (2,n):
			if ((n % i) == 0): 
				primo = 0         
	return (primo)

print "Introduzca el limite:"
limite = int (raw_input())

for p in range (2,limite+1):
  for q in range (2,limite+1):
		if ((esprimo (p) == 1) and (esprimo(q) == 1)):
			if (q == (p+2)):
				print "Los numeros", p, "y", q, "son primos gemelos"


