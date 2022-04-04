# Calculando o Perimetro e informando o maior lado de um triângulo


class Triangulo:

    ladoA = None
    ladoB = None
    ladoC = None

    def __init__(self,ladoA,ladoB,ladoC):
        self.ladoA = ladoA
        self.ladoB = ladoB
        self.ladoC = ladoC

    def calculaPerimetro(self):
        return self.ladoA + self.ladoB + self.ladoC

    def getMaiorLado(self):

        if (self.ladoA > self.ladoB) and (self.ladoA > self.ladoC):
            print(f'O maior lado é o ladoA = {self.ladoA}')

        elif (self.ladoB > self.ladoA) and (self.ladoB > self.ladoC):
            print(f'O maior lado é o ladoB = {self.ladoB}')

        else:
            print(f'O maior lado é o ladoC = {self.ladoC}')