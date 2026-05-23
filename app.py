from modelos.restaurante import Restaurante

restaurante_praca = Restaurante('Praça', 'Comida Caseira')
#restaurante_praca.receber_avaliacao('João', 10)
#restaurante_praca.receber_avaliacao('Maria', 8)
#restaurante_praca.receber_avaliacao('Carlos', 2)

def main():
    Restaurante.listar_restaurantes()
if __name__ == "__main__":
    main()