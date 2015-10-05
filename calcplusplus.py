#!/usr/bin/env python3

import sys
import csv
import calcoohija

calc = calcoohija.CalculadoraHija()


with open(sys.argv[1]) as fichero:
    contenido = csv.reader(fichero)
    
    resultado = 0
    for row in contenido:
        if row[0] == "suma":
            for elemento in row[1:]:
                resultado = calc.plus(int(resultado), int(elemento))
            print(resultado)
        if row[0] == "resta":
            resultado = calc.minus(int(row[1]), int(row[2]))
            for elemento in row[3:]:
                resultado = calc.minus(int(resultado), int(elemento))
            print(resultado)
        if row[0] == "divide":
            resultado = row[1]
            for elemento in row[2:]:
                if elemento == 0:
                    sys.exit("Division by zero is not allowed")
                else:
                    resultado = calc.div(int(resultado), int(elemento))
            print(resultado)
        if row[0] == "multiplica":
            resultado = calc.mult(int(row[1]), int(row[2]))
            for elemento in row[3:]:
                resultado = calc.mult(int(resultado), int(elemento))
            print(resultado)
