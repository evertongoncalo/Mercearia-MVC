from models import *
from dao import *
from datetime import datetime

class ControllerCategoria:
    def cadastra_categoria(self, nova_categoria):
        existe = False
        x = DaoCategoria.ler()
        for i in x:
            if i.categoria == nova_categoria:
                existe = True
        if not existe:
            DaoCategoria.salvar(nova_categoria)
            print("Categori salva com sucesso")
        else:
            print("Categoria já Existe")
                



a = ControllerCategoria()

a.cadastra_categoria("Frutas")         
                