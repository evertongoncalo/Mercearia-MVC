"""A model é onde defini-se as caracteristicas dos dados por meio das classes, entenda-se como os tipos que serão guardados no banco de dados dos sujeitos e ações"""

from datetime import datetime

class Categoria:
    def __init__(self, categoria):
        self.categoria = categoria
        
class Produtos:
    
    def __init__(self, nome, descricao, preco, categoria):
        self.nome = nome
        self.descricao = descricao
        self.preco = preco
        self.categoria = categoria
       
class Fornecedor:
    def __init__(self, empresa, telefone, nif, categoria):
        self.empresa = empresa
        self.telefone = telefone
        self.nif = nif
        self.categoria = categoria
        
class Estoque:
    def __init__(self, produto:Produtos, quantidade, fornecedor):
        self.produto = produto
        self.quantidade = quantidade
        self.fornecedor = fornecedor
        

        
        
class Venda:
    def __init__(self, item_vendido:Produtos, quantidade_vendida, vendedor, comprador, data=datetime.now().strftime('%d/%m/%Y')):
        self.item_vendido = item_vendido
        self.quantidade_vendida = quantidade_vendida
        self.vendedor = vendedor
        self.comprador = comprador
        self.data = data
        
        
class Pessoa:
    def __init__(self, nome, nif, endereco, telefone, email):
        self.nome = nome
        self.nif = nif
        self.endereco = endereco
        self.telefone = telefone
        self.email = email


class Vendedor(Pessoa):
    def __init__(self, nome, nif, endereco, telefone, email, id_vendedor):
        self.id_vendedor = id_vendedor
        super(Vendedor, self).__init__(nome, nif, endereco, telefone, email)
       
        
        

        
        
