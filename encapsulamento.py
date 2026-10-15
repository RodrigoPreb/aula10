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
  
  def trocar_senha(self, senha_atual:str, nova_senha:str) -> bool:
    """Trocar senha do cofre"""
    if senha_atual == self.__senha:
      self.__senha = nova_senha
      print("Senha alterada com sucesso")
      return True
  
    print("Senha incorreta! Não foi possível alterar a senha")
    return False
      
cofre = Cofre("cleitonC1")
cofre.abrir("errada")
cofre.abrir("cleitonC1")
cofre.trocar_senha("cleitonC1", "cleitonC15Anos!")
cofre.abrir("cleitonC1")
cofre.abrir("cleitonC15Anos!")


