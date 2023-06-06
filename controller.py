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
            
    def remover_categoria(self, remove_cat):
        x = DaoCategoria.ler()
        cat = list(filter(lambda x: x.categoria == remove_cat, x))
        
        if len(cat) <= 0:
            print('A categoria não existe')
        else:
            for i in range(len(x)):
                if x[i].categoria == remove_cat:
                    del x[i]
                    break
            print('Categoria removida com sucesso')
        with open ('dados/categoria.txt', 'w') as arq:
            for i in x:
                arq.writelines(i.categoria)
                arq.writelines("\n")
                
    def alterar_categoria(self, categoria_alterar, cat_alterada):
        x = DaoCategoria.ler()
        cat = list(filter(lambda x: x.categoria == categoria_alterar, x))
        
        if len(cat) > 0:
            cat1 = list(filter(lambda x: x.categoria == cat_alterada, x))
            if len(cat1) == 0:
                x = list(map(lambda x: Categoria(cat_alterada) if (x.categoria == categoria_alterar)else(x), x))
                print(f'Categoria alterada com sucesso, de: {categoria_alterar} para: {cat_alterada}')
            else:
                print('A Categoria já existe')
                
        else:
            print('A Categoria não existe')
        with open ('dados/categoria.txt', 'w') as arq:
            for i in x:
                arq.writelines(i.categoria)
                arq.writelines("\n")
               

    def mostrar_categoria(self):
        categoria = DaoCategoria.ler()
        
        if len(categoria) == 0:
            print("Categorias Vazia")
                
        else:
            for i in categoria:
                print(i.categoria)


class ControllerEstoque:
    def cadastrar_produto(self, produto, descricao, preco, categoria, quantidade, fornecedor):
        y = DaoEstoque.ler()
        h = DaoCategoria.ler()
        j = list(filter(lambda x: x.categoria == categoria, h))
        est = list(filter(lambda x: x.produto.produto == produto, y))

        if len(j) > 0:
            if len(est) == 0:
                produt = Produtos(produto, descricao, preco,categoria)
                esto = Estoque(produt,quantidade,fornecedor)
                DaoEstoque.salvar(esto)
                print("Produto cadastrado")
            else:
                print("Produto já existe!")
        else:
            print("Categoria não existe")
            
            
    def remover_produto(self, nome): #parametro de por onde deseja remover
        x = DaoEstoque.ler()
        est = list(filter(lambda x: x.produto.nome == nome, x))
        
        if len(est) > 0:
            for i in range(len(x)):
                if x[i].produto.nome == nome:
                    del x[i]
                    break 
            print("produto removido com sucesso")              
            
        else:
            print('produto não existe')
            
        with open('dados/estoque.txt', 'w') as arq:
            for i in x:
                arq.writelines(i.produto.nome + "|" + i.produto.descricao + "|" + str(i.produto.preco) + "|" + i.produto.categoria + "|" + str(i.quantidade) + "|" + i.fornecedor)
                arq.writelines("\n")
            
        
a = ControllerEstoque()
a.remover_produto("Arroz")


    

   
                