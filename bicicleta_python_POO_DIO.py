class Bicicleta:
  def __init__(self, cor, modelo, ano, valor):  
    self.cor = cor 
    self.modelo = modelo
    self.ano = ano
    self.valor = valor

  def buzinar(self):
    print("plim plim....")

  def parar(self):
    print("pararando bicicleta....")

  def correr(self):
    print("vrmmm....")

      
b1 = Bicicleta("vermelha", "caloi", 2022, 600)
b1.buzinar()
b1.correr()
b1.parar()
print(b1.cor, b1.modelo, b1.ano, b1.valor)

b2 = Bicicleta("verde", "monark", 2000, 189)
Bicicleta.buzinar(b2)

#20:13