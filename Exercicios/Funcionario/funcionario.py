class Funcionario:

    nome: None
    salario: None

    def __init__(self, nome, salario):

        self.nome = nome
        self.salario = salario

    def aumentarSalario(self,porcentualDeAumento):

        return ((porcentualDeAumento / 100) * self.salario) + self.salario