#!/usr/bin/python3
# -*- coding: utf-8 -*-
import sys
class Calculadora:

    def __init__(self, operador, operando1, operando2):
      "Esto es el método iniciliazador"
      self.operador = operador
      self.operando1 = operando1
      self.operando2 = operando2
      # No me dejaba imprimir operar, resta o suma directamente
      # por eso creo este atributo "solucion"
      self.solucion = 0

    def suma (self):
        self.solucion = self.operando1 + self.operando2

    def resta (self):
        self.solucion = self.operando1 - self.operando2

    def operar (self):

         if self.operador == "suma":
             self.suma()
         elif self.operador == "resta":
             self.resta()
         else:
             sys.exit('Operación sólo puede ser sumar o restar.')

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print()
        sys.exit("Usage : $ python3 operando1 operador operando2")
    try:
        operando1 = int(sys.argv[1])
        operando2 = int(sys.argv[3])
    except ValueError:
        sys.exit("Error: Non numerical parameters")
    operador = (sys.argv[2])
    Calc = Calculadora(operador,operando1,operando2)
    Calc.operar()
    print(Calc.solucion)
