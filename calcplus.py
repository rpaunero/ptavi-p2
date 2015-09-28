#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
import calcoohija

fichero = sys.argv[1]
fich = open(fichero,'r')
lineas = fich.readlines()

for linea in lineas:
	linea = linea[:-1]
	for elemento in linea:
		if elemento[0] == "suma":
			resultado = calc.plus(elemento[1], elemento[2])
		elif elemento[0] == "resta":
		elif elemento[0] == "divide":
		elif elemento[0] == "multiplica":

print(lines)
