class portfolio:
  def __init__(self, imagens, descricao,):
      self.imagens = imagens
      self.descricao = descricao
      
  def get_imagens(self,operador):
       if operador == self or operador.nivel == "adm":
           return self.imagens
        
  def get_descricao(self,operador):
       if operador == self or operador.nivel == "adm":
           return self.descricao
