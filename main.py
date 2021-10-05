from Desktop import Desktop
from Notebook import Notebook

d1 = Desktop(10,None,None,None)
d1.modelo = 'Intel'
d1.cor = 'Preto'
d1.preco = 3000
d1.getInformacoes()
d1.cadastrar()

print("---------------------------------")

n1 = Notebook(2000,None,None,None)
n1.modelo = 'Acer'
n1.cor = "Cinza"
n1.preco = 4000
n1.getInformacoes()
n1.cadastrar()