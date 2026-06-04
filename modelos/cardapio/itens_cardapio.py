class ItemCardapio:
    def __init__(self, nome: str, preco: float):
        self.__nome = nome
        self.__preco = preco

    def __str__(self):
        return f"{self.__nome} - R${self.__preco:.2f}"