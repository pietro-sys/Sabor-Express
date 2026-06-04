from modelos.cardapio.itens_cardapio import ItemCardapio

class Bebida(ItemCardapio):
    def __init__(self, nome: str, preco: float, tamanho: str):
        super().__init__(nome, preco)
        self.__tamanho = tamanho

    def __str__(self):
        return self.__nome