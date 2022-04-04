'''
    1. Construa uma classe Produto, que deve ter os atributos privados:
        - codigo
        - preco
       Adicione também um atributo estático
        - qtd_prod -  que deverá ser acrescentado toda vez que um novo objeto é criado.
       Crie os métodos get e set e teste a classe.   
'''
from produto import Produto

produto_1 = Produto(1, 'Caderno', 22.00 )
produto_2 = Produto(32, 'Camiseta', 44.56)

print(f'Código {produto_1.get_nome()}: {produto_1.get_codigo()} \nPreço {produto_1.get_nome()}: {produto_1.get_preco()} \n ')

print('\n','#$#' * 25,'\n')

print(f'Código {produto_2.get_nome()}: {produto_2.get_codigo()} \nPreço {produto_2.get_nome()}: {produto_2.get_preco()}')

print('\n','#$#' * 25,'\n')

print(f"Total Produtos: {produto_1.qtd_prod}")