#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
import calcoohija

fichero = sys.argv[1]
fich = open(fichero,'r')
lineas = fich.readlines()
calc = calcoohija.CalculadoraHija()

#resultado_suma = 0
#resultado_resta = 0
#resultado_division = 0
#resultado_multiplicacion = 0
for linea in lineas:
	#print(linea)
	linea = linea[:-1]
	dato = linea.split(',')
	if dato[0] == "suma":
		for elemento in dato[1:]:
			resultado = calc.plus(int(resultado), int(elemento))
		print('suma= ',resultado_suma)
	if dato[0] == "resta":
		resultado = calc.minus(int(dato[1]), int(dato[2]))
		for elemento in dato[3:]:
			resultado = calc.minus(int(resultado), int(elemento))
		print('resta=', resultado_resta)
	if dato[0] == "divide":
		resultado = calc.div(int(dato[1]), int(dato[2]))
		for elemento in dato[3:]:
			if elemento == 0:
				sys.exit("Division by zero is not allowed")
			else:
				resultado = calc.div(int(resultado), int(elemento))
		print('division=' ,resultado)
	if dato[0] == "multiplica":
		resultado = calc.mult(int(dato[1]), int(dato[2]))
		for elemento in dato[3:]:
			resultado = calc.mult(int(resultado), int(elemento))
		print('multiplicacion=', resultado)
