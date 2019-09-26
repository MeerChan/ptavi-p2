
#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
import calcoo


class CalculadoraHija(calcoo.Calculadora):
    def mult(operando1, operando2, solucion):
        """ Function to multiply the operands. Ops have to be ints """
        solucion = operando1 * operando2

    def div(operando1, operando2, solucion):
        """ Function to split the operands """
        try:
            solucion = operando1/operando2
        except ZeroDivisionError:
            sys.exit("Division by zero is not allowed")

    def operar2(self):
        #Paso el objeto calc luego
        if self.operador == "dividir":
            CalculadoraHija.div(self.operando1, self.operando2, self.solucion)
        elif self.operador == "multiplicar":
            CalculadoraHija.mult(self.operando1, self.operando2, self.solucion)
        else:
            sys.exit('Operación sólo puede ser divide o mult.')

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print()
        sys.exit("Usage : $ python3 operando1 operador operando2")
    try:
        operando1 = int(sys.argv[1])
        operando2 = int(sys.argv[3])
    except ValueError:
        sys.exit("Error: Non numerical parameters")
    operador = sys.argv[2]
    Calc = calcoo.Calculadora(operador,operando1,operando2)
    if (operador == "suma") or (operador == "resta"):
        Calc.operar()
    elif operador == "multiplicar" or (operador == "dividir"):
        CalculadoraHija.operar2(Calc)
    else:
        sys.exit('Operación sólo puede ser suma, resta, multiplicar o dividir')
print(Calc.solucion)
