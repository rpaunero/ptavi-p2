#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
import calcoohija


fichero = sys.argv[1]
fich = open(fichero, 'r')
lineas = fich.readlines()
calc = calcoohija.CalculadoraHija()

resultado = 0
for linea in lineas:
    linea = linea[:-1]
    dato = linea.split(',')
    if dato[0] == "suma":
        for elemento in dato[1:]:
            resultado = calc.plus(int(resultado), int(elemento))
        print(resultado)
    if dato[0] == "resta":
        resultado = calc.minus(int(dato[1]), int(dato[2]))
        for elemento in dato[3:]:
            resultado = calc.minus(int(resultado), int(elemento))
        print(resultado)
    if dato[0] == "divide":
        #resultado = calc.div(int(dato[1]), int(dato[2]))
        resultado = dato[1]
        for elemento in dato[2:]:
            if elemento == 0:
                sys.exit("Division by zero is not allowed")
            else:
                resultado = calc.div(int(resultado), int(elemento))
        print(resultado)
    if dato[0] == "multiplica":
        resultado = calc.mult(int(dato[1]), int(dato[2]))
        for elemento in dato[3:]:
            resultado = calc.mult(int(resultado), int(elemento))
        print(resultado)
