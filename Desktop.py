from Computador import Computador

class Desktop(Computador):
  def __init__(self,potenciaDaFonte, modelo, cor, preco):
    self._potenciaDaFonte = potenciaDaFonte
    self.modelo = modelo
    self.cor = cor
    self.preco = preco

  @property
  def potenciaDaFonte(self):
    return self._potenciaDaFonte

  @potenciaDaFonte.setter
  def potenciaDaFonte(self,valor):
    self._potenciaDaFonte = valor

  def getInformacoes(self):
    print("Potência da Fonte: ", self._potenciaDaFonte)
    super().getInformacoes()

  def cadastrar(self):
    print("Desktop cadastrado com sucesso.")