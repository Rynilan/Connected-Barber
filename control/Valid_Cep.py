import re

class BuscaEndereco:

    def __init__(self, cep):
        cep = str(cep)
        if self.cep_eh_Valido(cep):
            self.cep = cep
        else:
            raise ValueError("CEP inválido!")

    def cep_eh_Valido(self, cep):
       if len(cep) == 8:
          padrao_cep = re.compile(r'(\d){5}(\d){3}')

          match = padrao_cep.match(cep)

          return True
       else:
          return False