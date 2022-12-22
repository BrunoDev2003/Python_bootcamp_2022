class Pessoa:
  def __init__(self,nome,idade):
    self.nome = nome
    self.idade = idade

  @classmethod
  def criar_apartir_data_nasicmento(cls,ano,mes,dia,nome):
    idade = 2022 - ano
    return cls(nome,idade)

  @staticmethod
  def e_maior_iddae(idade):
    return idade >= 18

#p = Pessoa("Bruno", 19)
#print(p.nome,p.idade)

p2 = Pessoa().criar_apartir_data_nasicmento(2003, 7, 1, "bruno")
print(p2.nome,p2.idade)

print(Pessoa.e_maior_iddae(10))
print(Pessoa.e_maior_iddae(19))