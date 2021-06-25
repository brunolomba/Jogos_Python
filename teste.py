class Escritor:
    def __init__(self, nome):
        self.nome = nome
        self.ferramenta = None

    @property
    def ferramenta(self):
        return self.ferramenta

    @ferramenta.setter
    def ferramenta(self, ferramenta):
        self.ferramenta = ferramenta

class Caneta:
    def __init__(self, marca):
        self.marca = marca

    def escever():
        print('Caneta escrevendo...')

# escritor = Escritor('Bruno')
caneta = Caneta('Bic')
escritor.ferramenta = caneta


escrito.ferramenta.escever()