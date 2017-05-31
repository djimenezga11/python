import random

class Boomerang(object):
    def __init__(self):
        self.quita = 0
        self.nombre = "Boomerang"

    def devAtaque(self, origen):
        if origen.dano<10:
            return 0
        else:
            self.quita = random.randrange(11,16)+origen.inteligencia
            origen.dano