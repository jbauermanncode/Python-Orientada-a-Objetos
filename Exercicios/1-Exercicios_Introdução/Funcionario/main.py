'''    2. Classe Funcionário: Implemente a classe funcionário. Um funcionário
    tem um nome e um salário. Escreva um construtor com dois parametros
    (nome e salário) e o método aumentarSalario(porcentualDeAumento) que 
    aumente o salário do funcionário em uma certa porcentagem. Exemplo
    de uso:

        harry = Funcionario('Harry', 25000)

        harry.aumentarSalario(10)

    Faça um programa que teste o método da classe.'''


from funcionario import Funcionario

harry = Funcionario('Harry', 10000)
print(harry.aumentarSalario(20))