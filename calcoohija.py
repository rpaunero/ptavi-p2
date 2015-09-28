#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
import calcoo
	
class CalculadoraHija(calcoo.Calculadora):
	def mult(self, op1, op2):
		return op1 * op2

	def div(self, op1, op2):
		return op1 / op2

	

if __name__ == "__main__":
	try:
		operando1 = int(sys.argv[1])
		operando2 = int(sys.argv[3])
	except ValueError:
		sys.exit("Error: Non numerical parameters")

	calc = CalculadoraHija()


	if sys.argv[2] == "suma":
		result = calc.plus(operando1, operando2)
	elif sys.argv[2] == "resta":
		result = calc.minus(operando1, operando2)
	elif sys.argv[2] == "multiplica":
		result = calc.mult(operando1, operando2)
	elif sys.argv[2] == "divide":
			if operando2 == 0:
				sys.exit("Division by zero is not allowed")
			else:
				result = calc.div(operando1, operando2)
	print(result)
