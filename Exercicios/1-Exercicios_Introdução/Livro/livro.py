class Livro:

    def __init__(self, nome, autor, qtd_paginas):
        self.nome = nome
        self.autor = autor
        self.qtd_paginas = qtd_paginas
        self.preco = 0

    def get_preco(self):
        return self.preco

    def set_preco(self, preco):
        self.preco = preco
