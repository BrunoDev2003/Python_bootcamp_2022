class Animal:
  pass


class Mamifero(Animal):
  def __init__(self, cor_bico, **kw):
    self.cor_bico = cor_bico
    super().__init__(**kw)


class Cachorro(Mamifero)