from fabricante import *
from cadastro import *
class Lista:
    def __init__(self):
        self.listaProdutos = []
        self.lista_de_fabricantes = []
    def cadastrar_produto(self):
        entrada_cod = input('INFORME O CODIGO                           =')
        entrada_descricao = input('INFORME A DESCRICAO                           =')
        entrada_fabricante = input('informe o fabricante                                  =')
        entrada_quantidade = int(input('informe a quantidade                                          ='))
        self.listaProdutos.append(Cadastro(cod=entrada_cod,descricao= entrada_descricao,quantidade = entrada_quantidade,fabricante= entrada_fabricante))
        print('')





    def lista_produtos(self):
        for i in range(len(self.listaProdutos)):
            print( self.listaProdutos[i].cod,
            self.listaProdutos[i].descricao,
            self.listaProdutos[i].quantidade,
            self.listaProdutos[i].fabricante)

    def listar_cod(self):
        for i in range(len(self.listaProdutos)):
            print(self.listaProdutos[i].cod)

    def alterar_descricao(self):
        entrada = input('informe o codigo                                 = ')
        for i in range ( len (self.listaProdutos)):
            if entrada ==self.listaProdutos[i].cod:
                self.listaProdutos[i].descricao = input(' nova descricao                               = ')
            else:
                print('codigo do produto nao encontrado                                            =')

    def procurar(self):
        entrada = input('informe o codigo                                                            = ')
        for i in range(len(self.listaProdutos)):
            if entrada == self.listaProdutos[i].cod:
                print('codigo encontrado                                                 =',self.listaProdutos[i].cod)
            else:
                print('codigo do produto nao encontrado                                    = ')








    def cadastrar_fabricante(self):
        self.lista_de_fabricantes.append(Fabricante())


    def mostrar_fabricantes(self):
        for i in range (len( self.lista_de_fabricantes)):
            print( self.lista_de_fabricantes[i].nome)