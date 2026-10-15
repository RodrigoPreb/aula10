class Pessoa:
  def __init__(self, nome:str, idade:int) -> None:
    self.nome = nome
    self._idade = idade
    
fulano = Pessoa("Fulano", 30)

print(fulano.nome)
fulano._idade = -5
print(fulano._idade)