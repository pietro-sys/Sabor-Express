from modelos.cardapio.itens_cardapio import ItemCardapio

class Prato(ItemCardapio):
    def __init__(self, nome, preco, descricao):
        super().__init__(nome, preco)
        self.__descricao = descricao

    def __str__(self):
        return self.__nome