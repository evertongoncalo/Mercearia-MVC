"""A model é onde defini-se as caracteristicas dos dados por meio das classes, entenda-se como os tipos que serão guardados no banco de dados"""

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
       
        
class Estoque:
    def __init__(self, produto:Produtos, quantidade, fornecedor, status):
        self.produto = produto
        self.quantidade = quantidade
        self.fornecedor = fornecedor
        self.status = status
        
        
class Venda:
    def __init__(self, item_vendido:Produtos, quantidade_vendida, vendedor, comprador):
        self.item_vendido = item_vendido
        self.quantidade_vendida = quantidade_vendida
        self.vendedor = vendedor
        self.comprador = comprador
        self.data = datetime
        

        
        
