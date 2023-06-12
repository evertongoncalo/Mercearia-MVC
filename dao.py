"DATA ACCESS OBJECT"
"""serve como armazenamento e leitura, como um getter and setter"""

from models import *


class DaoCategoria:
    @classmethod
    def salvar(cls, categoria):
        with open('dados/categoria.txt', 'a') as arq:
            arq.writelines(categoria)
            arq.writelines("\n")
    
    @classmethod
    def ler(cls):
        with open('dados/categoria.txt', 'r') as arq:
            cls.categoria = arq.readlines()
            
            cls.categoria = list(map(lambda x: x.replace("\n", ""), cls.categoria))
        cat = []
        for i in cls.categoria:
            cat.append(Categoria(i))
        return cat  

class DaoVenda:
    @classmethod
    def salvar(cls, venda: Venda):  #aqui +assa a instancia da model
        with open('dados/venda.txt', 'a') as arq:
            arq.writelines(venda.item_vendido.nome + "|" + venda.item_vendido.descricao + "|" + str(venda.item_vendido.preco) + "|" + venda.item_vendido.categoria + "|" + str(venda.quantidade_vendida) + "|" + venda.vendedor + "|" + venda.comprador + "|" + venda.data)
            arq.writelines("\n")
    @classmethod
    def ler(cls):
        with open('dados/venda.txt', 'r') as arq:
            cls.venda = arq.readlines()
            
            cls.venda = list(map(lambda x: x.replace("\n", ""), cls.venda))
            cls.venda = list(map(lambda x: x.split("|"), cls.venda))
            
            vend = []  # Crie uma lista vazia para armazenar as vendas
            for i in cls.venda:
                vend.append(Venda(Produtos(i[0], i[1], i[2], int(i[3])), int(i[4]), i[5], i[6]))
            return vend
        
class DaoEstoque:
    @classmethod
    def salvar(cls, estoque: Estoque):  #aqui +assa a instancia da model
        with open('dados/estoque.txt', 'a') as arq:
            arq.writelines(estoque.produto.nome + "|" + estoque.produto.descricao + "|" + str(estoque.produto.preco) + "|" + estoque.produto.categoria + "|" + str(estoque.quantidade) + "|" + estoque.fornecedor)
            arq.writelines("\n")
    @classmethod
    def ler(cls):
        with open('dados/estoque.txt', 'r') as arq:
            cls.estoque = arq.readlines()
            
            cls.estoque = list(map(lambda x: x.replace("\n", ""), cls.estoque))
            cls.estoque = list(map(lambda x: x.split("|"), cls.estoque))
            
            est = []  # Crie uma lista vazia para armazenar as estoques
            for i in cls.estoque:
                est.append(Estoque(Produtos(i[0], i[1], i[2], i[3]), i[4], i[5]))
            return est

        
     



class DaoFornecedor:
    @classmethod
    def salvar(cls, fornecedor: Fornecedor):
        with open('dados/fornecedor.txt', 'a') as arq:
            arq.writelines(fornecedor.empresa + "|" + str(fornecedor.telefone) + "|" + str(fornecedor.nif) + "|" + fornecedor.categoria) 
            arq.writelines("\n")
            
    def ler(cls):
        with open('dados/fornecedor.txt', 'r') as arq:
            cls.fornecedor = arq.readlines()
            
            cls.fornecedor = list(map(lambda x: x.replace("\n", ""), cls.fornecedor))
            cls.fornecedor = list(map(lambda x: x.split("|"), cls.fornecedor))
            
            forn = []  # Crie uma lista vazia para armazenar as fornecedors
            for i in cls.fornecedor:
                forn.append(Fornecedor(i[0], i[1], i[2], i[3]))
            return forn
        
class DaoCliente:
    @classmethod
    def salvar(cls, cliente: Pessoa):
        with open('dados/clientes.txt', 'a') as arq:
            arq.writelines(cliente.nome + "|" + str(cliente.nif) + "|" + cliente.endereco + "|" + str(cliente.telefone) + "|" + cliente.email) 
            arq.writelines("\n")
            
    def ler(cls):
        with open('dados/clientes.txt', 'r') as arq:
            cls.cliente = arq.readlines()
            
            cls.cliente = list(map(lambda x: x.replace("\n", ""), cls.cliente))
            cls.cliente = list(map(lambda x: x.split("|"), cls.cliente))
            
            cli = []  # Crie uma lista vazia para armazenar as clientes
            for i in cls.cliente:
                cli.append(Pessoa(i[0], i[1], i[2], i[3], i[4]))
            return cli
        

class DaoVendedor:
    def salvar(cls, vendedor: Vendedor):
        with open('dados/vendedor.txt', 'a') as arq:
            arq.writelines(vendedor.nome + "|" + str(vendedor.nif) + "|" + vendedor.endereco + "|" + str(vendedor.telefone) + "|" + vendedor.email + "|" + str(vendedor.id_vendedor))
            arq.writelines("\n")
    def ler(cls):
        with open('dados/vendedor.txt', 'r') as arq:
            cls.vendedor = arq.readlines()
            
            cls.vendedor = list(map(lambda x: x.replace("\n", ""), cls.vendedor))
            cls.vendedor = list(map(lambda x: x.split("|"), cls.vendedor))
            
            vend = []  # Crie uma lista vazia para armazenar as vendedors
            for i in cls.vendedor:
                vend.append(Pessoa(i[0], i[1], i[2], i[3], i[4], i[5]))
            return vend
        
        
        
"""x = "Frutas"
DaoCategoria.salvar(x)"""