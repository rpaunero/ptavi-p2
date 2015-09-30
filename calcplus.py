#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
import calcoohija

fichero = sys.argv[1]
fich = open(fichero,'r')
lineas = fich.readlines()
calc = calcoohija.CalculadoraHija()

resultado = 0
for linea in lineas:
	linea = linea[:-1]
	#print(linea)
	dato = linea.split(',')
	#print(dato)
	if dato[0] == "suma":
		#print("linea[0] = suma")
		for elemento in dato[1:]:
			resultado = calc.plus(int(resultado), int(elemento))
	print(resultado)
	elif dato[0] == "resta":
		result = calc.minus(int(dato[1]), int(dato[2]))
		for elemento in dato[1:]:
			resultado = calc.minus(int(result), int(elemento))
	print(resultado)
	elif dato[0] == "divide":
		for elemento in dato[1:]:
			if elemento == 0:
				sys.exit("Division by zero is not allowed")
			else:
				resultado = calc.div(int(resultado), int(elemento))
	print(resultado)
	elif dato[0] == "multiplica":
		for elemento in dato[1:]:
			resultado = calc.mult(int(resultado), int(elemento))
	print(resultado)
#print(lines)
