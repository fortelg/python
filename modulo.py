#!/usr/bin/python
#!encoding: UTF-8

nombre = []
direccion = []
precio_medio = []
tipo_comida = []
diccionario = {"nombre": nombre, "direccion":direccion, "precio_medio": precio_medio, "tipo_comida":tipo_comida}

def introducir_datos():
	print "Introduzca el nombre del restaurante:"
	nombre.append (raw_input())
	print "Introduzca la direccion del restaurante:"
	direccion.append (raw_input())
	print "Introduzca el precio medio del restaurante:"
	precio_medio.append (float (raw_input()))
	print "Introduzca el tipo de comida del restaurante:"
	tipo_comida.append (raw_input())

def mostrar_datos():
	for i in range (len (nombre)):
		print "Nombre del restaurante:", diccionario["nombre"][i]
		print "Direccion del restaurante:", diccionario["direccion"][i]
		print "Precio medio del restaurante:", diccionario["precio_medio"][i]
		print "Tipo de comida del restaurante:", diccionario["tipo_comida"][i]

def ordenar_datos():
	b = []
	for i in range (len (nombre)):
		a = []
		a.append (diccionario["nombre"][i])
		a.append (diccionario["direccion"][i])
		a.append (diccionario["precio_medio"][i])
		a.append (diccionario["tipo_comida"][i])
		b.append (a);
	estructura_ordenada  = sorted(b, key=lambda c : c[2])
	print "DATOS ORDENADOS POR PRECIO"
	for i in range (len (nombre)):
		print "Nombre del restaurante:", estructura_ordenada[i][0]
		print "Direccion del restaurante:", estructura_ordenada[i][1]
		print "Precio medio del restaurante:", estructura_ordenada[i][2]
		print "Tipo de comida del restaurante:", estructura_ordenada[i][3]

def ordenar_datos_tipo_comida():
	print "Introduzca el tipo de comida a buscar:"
	tcomida = raw_input()
	b = []
	for i in range (len (nombre)):
		a = []
		if (diccionario["tipo_comida"][i] == tcomida):
			a.append (diccionario["nombre"][i])
			a.append (diccionario["direccion"][i])
			a.append (diccionario["precio_medio"][i])
			a.append (diccionario["tipo_comida"][i])
			b.append (a);
	if (len(b) > 0):
		estructura_ordenada  = sorted(b, key=lambda c : c[2])
		print "DATOS ORDENADOS POR PRECIO"
		for i in range (len (b)):
			print "Nombre del restaurante:", estructura_ordenada[i][0]
			print "Direccion del restaurante:", estructura_ordenada[i][1]
			print "Precio medio del restaurante:", estructura_ordenada[i][2]
			print "Tipo de comida del restaurante:", estructura_ordenada[i][3]
	else:
		print "No hay restaurantes con ese tipo de comida"

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
			introducir_datos()
		elif (opcion == 2):
			mostrar_datos()
		elif (opcion == 3):
			ordenar_datos()
		elif (opcion == 4):
			ordenar_datos_tipo_comida()

if (__name__ == "__main__"):
	menu()
