class Cofre:
  def __init__(self, senha:str) -> None:
    self.__senha = senha #_ _ privado name nangling
    self.__tentativa = 0
    
  def abrir(self, senha:str) -> bool:
    """Tentar Abrir Cofre Com a Senha fornecida"""
    self.__tentativa += 1
    
    if senha == self.__senha:
      print("Cofre Aberto!")
      return True
    
    print(f"Senha Incorreta! Tentativa {self.__tentativa}")
    return False
  
cofre = Cofre("cleitonC1")
cofre.abrir("errada")
cofre.abrir("cleitonC1")

