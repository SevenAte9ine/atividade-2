from Computador import Computador

class Notebook(Computador):
  def __init__(self,tempoDeBateria, modelo, cor, preco):
    self.__tempoDeBateria = tempoDeBateria
    self.modelo = modelo
    self.cor = cor
    self.preco = preco

  @property
  def tempoDeBateria(self):
    return self.__tempoDeBateria

  @tempoDeBateria.setter
  def tempoDeBateria(self, valor):
    admin = True
    if admin:
      self.__tempoDeBateria = valor
    else:
      print("Açao não permitida")

  def getInformacoes(self):
    print("Tempo de Bateria: ", self.__tempoDeBateria)
    super().getInformacoes()

  def cadastrar(self):
    print("Notebook cadastrado com sucesso.")