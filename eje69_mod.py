#!/usr/bin/python
#!encoding: UTF-8
import modulo

def menu ():
	opcion = 1
	while (opcion != 0):
		print "1.- Introducir los datos de un Restaurante"
		print "2.- Mostrar la informacion almacenada"
		print "3.- Mostrar la informacion almacenada, ordenada por precio"
		print "4.- Buscar por tipo de comida"
		print "0.- Salir"
		print "Introduzca una opcion:"
		opcion = int (raw_input())
		if (opcion == 1):
			modulo.introducir_datos()
		elif (opcion == 2):
			modulo.mostrar_datos()
		elif (opcion == 3):
			modulo.ordenar_datos()
		elif (opcion == 4):
			modulo.ordenar_datos_tipo_comida()

menu()
print "\n"
