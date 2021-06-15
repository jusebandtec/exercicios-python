import math


class Quadrado:

    def __init__(self, tamanho_lado):
        self.tamanho_lado = tamanho_lado

    def muda_valor_lado(self, novo_tamanho_lado):
        self.tamanho_lado = novo_tamanho_lado

    def retornar_valor_lado(self):
        return self.tamanho_lado

    def calcular_area(self):
        return self.tamanho_lado * self.tamanho_lado

quadrado = Quadrado(5)
print(quadrado.retornar_valor_lado())
print(quadrado.calcular_area())
quadrado.muda_valor_lado(6)
print(quadrado.retornar_valor_lado())
print(quadrado.calcular_area())