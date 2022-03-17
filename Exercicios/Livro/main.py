from livro import Livro

livro = Livro('V de Vingança', 'Alan Moore', 200)
livro.set_preco(100.00)

print(f'Nome do Livro: {livro.nome} \nAutor: {livro.autor} \nQuantidade de páginas: {livro.qtd_paginas}')
print(f'Preço: {livro.get_preco():.2f}')