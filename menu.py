from venda import *
from compra import *

from lista import *

class Menu:
    def __init__(self):
        listinha = Lista()

        compra = Compra()
        compra.compras = listinha

        venda = Venda()
        venda.vender = listinha

        while True:
            entrada = input(
                'informe a opção desejada                        '
                '\n 0 - CADASTRAR                      '
                '\n1 - LISTAR PRODUTO                       '
                '\n 2 - PROCURAR PRODUTO                        '
                '\n3 - ALTERAR PRODUTO                        '
                '\n4 - SAIR                           '
                '\n 5 - COMPRAR                             '
                '\n 6 - VENDER                             '
                '\n 7 - CADASTRAR FABRICANTE                            '
                '\n 8 - MOSTRAR FABRICANTE                           '
                '=')

            if entrada =='0':
                listinha.cadastrar_produto()
            elif entrada == '1':
                listinha.lista_produtos()
            elif entrada == '2':
                listinha.procurar()
            elif entrada == '3':
                listinha.alterar_descricao()
            elif entrada == '4':
                break
            elif entrada == '5':
                compra.qt_comprado()
            elif entrada == '6':
                venda.vendido()
            elif entrada == '7':
                listinha.cadastrar_fabricante()
            elif entrada == '8':
                listinha.mostrar_fabricantes()
            else:
                print( "                                                    ERROR!!!!!!!!!!")


