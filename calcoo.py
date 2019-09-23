#!/usr/bin/python3
# -*- coding: utf-8 -*-
class Calculadora():

    def __init__(self, operador, operando1, operando2):
      "Esto es el método iniciliazador"
      self.operador = operador
      self.operando1 = operando1
      self.operando2 = operando2

  if __name__ == "__main__":
    objeto = Clase("pepe")






class CalculadoraHija(ClaseMadre):
  "Esto es un ejemplo de clase que hereda de ClaseMadre"

  def __init__(self, valor):
    "Esto es el método iniciliazador"
    self.atributo = valor

if __name__ == "__main__":
  objeto = Clase("pepe") # Creo un objeto de la clase Clase
                         # y le paso el valor pepe para su
                         # atributo en la inicialización
