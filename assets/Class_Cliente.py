import atores 
class Cliente (atores):
    
    super().__init__()

    def __init__(self, cep, preferencias):
        # Valida o CEP para garantir que ele tenha exatamente 11 caracteres
        if len(cep) != 11:
            raise ValueError("O CEP deve ter exatamente 11 caracteres.")
        
        self.cep = cep  # Armazena o CEP
        self.preferencias = tuple(preferencias)  # Armazena as preferências como tupla

    def __str__(self):
        return f"Cliente(CEP: {self.cep}, Preferências: {self.preferencias})"