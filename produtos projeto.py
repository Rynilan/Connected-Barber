import assets.oferecimentos.Oferecimento import Oferecimento
class produto(Oferecimento):
  def __init__(self,nome,descricao,foto,preco):
    super().__init__(nome,descricao,foto,preco)
    
  def __str__(self):
      
      return f"produto:{self.nome}, preço: R$:{self.preco:.2f}'
