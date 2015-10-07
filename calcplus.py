#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
import calcoohija

calc = calcoohija.CalculadoraHija()


def operacion(dato):
    dicc = {"suma": calc.plus, "resta": calc.minus,
            "multiplica": calc.mult, "divide": calc.div}

    if dato[0] == "suma":
        func = calc.plus
    elif dato[0] == "resta":
        func = calc.minus
    elif dato[0] == "multiplica":
        func = calc.mult
    elif dato[0] == "divide":
        func = calc.div
    resultado = dato[1]
    for elemento in dato[2:]:
        try:
            funcion = dicc[dato[0]]
            resultado = funcion(int(resultado), int(elemento))
        except ValueError:
            print("Error de valor en esta línea")
            break
    print(resultado)

if __name__ == "__main__":
    fichero = sys.argv[1]
    fich = open(fichero, 'r')
    lineas = fich.readlines()

    resultado = 0
    for linea in lineas:
        linea = linea[:-1]
        dato = linea.split(',')
        operador = dato[0]
        resultado = operacion(dato)
