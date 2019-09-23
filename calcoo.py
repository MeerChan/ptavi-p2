#!/usr/bin/python3
# -*- coding: utf-8 -*-
import sys
class Calculadora:

    def __init__(self, operador, operando1, operando2):
      "Esto es el método iniciliazador"
      self.operador = operador
      self.operando1 = operando1
      self.operando2 = operando2

    def suma (self):
        return self.operando1 + self.operando2

    def resta (self):
        return self.operando1 - self.operando2

    def operar (self):

         if self.operador == "suma":
             return self.suma
         elif self.operador == "resta":
             return self.resta
         else:
             sys.exit('Operación sólo puede ser sumar o restar.')

if __name__ == "__main__":
     try:
        operando1 = int(sys.argv[1])
        operando2 = int(sys.argv[3])
     except ValueError:
        sys.exit("Error: Non numerical parameters")
     operador = (sys.argv[2])
     Calc = Calculadora(operador,operando1,operando2)
     print(Calc.operador)
     print(Calc.operando1)
     print(Calc.operando2)
     print(Calc.resta)
     resultado = (Calc.operar)
     print(resultado)
