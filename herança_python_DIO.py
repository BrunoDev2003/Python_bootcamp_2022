class Veiculo:

  def __init__(self, cor, placa, numero_rodas):
    self.cor = cor
    self.placa = placa
    self.numero_rodas = numero_rodas

    def ligar_motor(self):
      print("ligando o motor")


class Motocicleta(Veiculo):
  pass


class Carro(Veiculo):
  pass


class Caminhao(Veiculo):
  pass


moto = Motocicleta("vermelha", "h1b2c4", 2)
print(moto)

#05:20