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
            
        
    def alterar_produtos(self, nomeAlterar, novoNome, novaDesc, novoPreco, novaCategoria, novaQuantidade, novoFornecedor):
        x = DaoEstoque.ler()
        y = DaoCategoria.ler()
        h = list(filter(lambda x: x.categoria == novaCategoria, y))
        if len(h)>0: #Se for mairo que zero é porque existe a categoria.
            est = list(filter(lambda x: x.produto.nome == nomeAlterar, x))
            if len(est)>0:
                est = list(filter(lambda x: x.produto.nome == novoNome, x))
                if len(est) == 0:
                    x = list(map(lambda x: Estoque(Produtos(novoNome,novaDesc,novoPreco,novaCategoria),novaQuantidade,novoFornecedor) if (x.produto.nome == nomeAlterar) else (x),x))
                    print("produto Alterado com sucesso")
                else:
                    print('O produto já existe')
                    
                with open('dados/estoque.txt', 'w') as arq:
                    for i in x:
                        arq.writelines(i.produto.nome + "|" + i.produto.descricao + "|" + str(i.produto.preco) + "|" + i.produto.categoria + "|" + str(i.quantidade) + "|" + i.fornecedor)
                        arq.writelines("\n")                  
                    
            else:
                print('O produto não existe')
        else:
            print("categoria inexistente")
    
    def mostrar_estoque(self):
        est = DaoEstoque.ler()
        
        if len(est) == 0:
            print("Estoque Vazio")
                
        else:
            for i in est:
                print(i.produto.nome + "|" + i.produto.descricao + "|" + str(i.produto.preco) + "|" + i.produto.categoria + "|" + str(i.quantidade) + "|" + i.fornecedor)


class ControllerVenda:
    def cadastrar_venda(self, nomeProduto, vendedor, comprador, quantidadeVendida):
        x = DaoEstoque.ler()
        temp = []
        existe = False
        quantidade = False
        
        for i in x:
            if existe == False:
                if i.produto.nome == nomeProduto:
                    existe = True
                    if int(i.quantidade) >= quantidadeVendida:
                        quantidade = True
                        i.quantidade = int(i.quantidade) - quantidadeVendida
                        
                        vendido = Venda(Produtos(i.produto.nome,i.produto.descricao,i.produto.preco,i.produto.categoria),quantidadeVendida,vendedor,comprador)
                        valorCompra = int(quantidadeVendida) * int(i.produto.preco)
                        DaoVenda.salvar(vendido)
                        
        temp.append([Produtos(i.produto.nome,i.produto.descricao,i.produto.preco,i.produto.categoria), i.quantidade])
        arq = open('dados/venda.txt', 'w')
        arq.write('')
        for i in temp:
            with open('estoque.txt','a') as arq:
                arq.writelines(i[0].nome + "|" + i[0].preco + "|" + i[0].categoria + "|" + str([i[1]]))
                arq.writelines("\n")
                
        if existe == False:
            print("O produto não existe")
            return None
        
        elif not quantidade:
            print("A quantidade vendida não tem em estoque")

        else:
            return valorCompra
            
            
a = ControllerVenda()
a.cadastrar_venda("Arroz","rui","Everton",1)
    

   
                