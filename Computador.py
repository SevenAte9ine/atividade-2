from abc import ABCMeta, abstractmethod, abstractproperty

class Computador(metaclass=ABCMeta):

  modelo = None
  cor = None
  preco = None

  def getInformacoes(self):
	  print("Modelo: " , self.modelo )
	  print("Ano: " , self.cor )
	  print("Ano: " , self.preco )

  @abstractmethod
  def cadastrar(self):
    pass
