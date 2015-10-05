#!/usr/bin/env python3

import sys
import csv
import calcoohija
import calcplus


if __name__ == "__main__":

    with open(sys.argv[1]) as fichero:
        contenido = csv.reader(fichero)

        for linea in contenido:
            calcplus.operacion(linea)
