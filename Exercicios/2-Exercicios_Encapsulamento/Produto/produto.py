class Produto:

    qtd_prod = 0

    def __init__(self, codigo, nome, preco):
        self.__codigo = codigo
        self.__nome = nome
        self.__preco = preco
        Produto.qtd_prod += 1

    def set_codigo(self, codigo):
        self.__codigo = codigo

    def set_nome(self, nome):
        self.__nome = nome

    def set_preco(self, preco):
        self.__preco = preco

    def get_codigo(self):
        return self.__codigo

    def get_nome(self):
        return self.__nome

    def get_preco(self):
        return self.__preco

    