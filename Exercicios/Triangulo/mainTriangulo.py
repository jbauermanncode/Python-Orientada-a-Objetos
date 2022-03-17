'''    1. Classe Triangulo: Crie uma classe que modele um triangulo:
        - Atributos: ladoA, ladoB, ladoC
        - Métodos: calcular Perímetro, getMaiorLado;

    Crie um programa que utilize esta classe. Ele deve pedir ao usuário que
    informe as medidas de um triangulo. Depois, deve criar um objeto com as
    medidas e imprimir sua área e maior lado.
'''


from trianguloExercicio import Triangulo

print('Informe as medidas de um triangulo:')
t = Triangulo(
    int(input('Digite um valor para o ladoA: ')),
    int(input('Digite um valor para o ladoB: ')),
    int(input('Digite um valor para o ladoC: ')))
print(f'O valor do perimetro é : {t.calculaPerimetro()}\n {t.getMaiorLado()}')




