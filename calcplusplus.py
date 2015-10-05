#!/usr/bin/env python3

import sys
import csv
import calcplus

calc = calcoohija.CalculadoraHija()
opera = operacion.calcplus()
resultado = 0

with open(sys.argv[1]) as fichero:
    contenido = csv.reader(fichero)

    for row in contenido:
     opera.operacion(row)

    resultado = operacion(dato)
