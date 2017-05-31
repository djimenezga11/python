import random
import Boomerang as boo

class Jugador(object):
    def __init__(self, nombre):
        self.nombre = nombre
        self.vida_max = random.randrange(50, 100)
        self.dano_max = random.randrange(20, 40)
        self.fuerza = random.randrange(5,10)
        self.inteligencia = random.randrange(2,5)
        self.vida = self.vida_max
        self.dano = self.dano_max
        self.habilidades = [Boomerang(), Golpear()]

    def __str__(self):

        return "Jugador: " +str(self.nombre)+" Vida: "+str(self.vida)+"/"+str(self.vida_max)+" Dano: "+str(self.dano)+"/"+str(self.dano_max)

    def estadisticas(self):
        print(self.nombre)
        print("Vida:", self.vida, "/", self.vida_max)
        print("Dano", self.dano, "/", self.dano_max)
        print("Fuerza:", self.fuerza)
        print("Inteligencia:",self.inteligencia)

    def eleccion(self):
        print("\nElige un ataque:\n")
        print("1 - Boomerang (10 dano)")
        print("2 - Golpear (5 dano)")
        x = input(">")
        return int(x)

class Jugador2(object):
    def __init__(self, nombre):
        self.nombre = nombre
        self.vida_max = random.randrange(50, 100)
        self.dano_max = random.randrange(20, 40)
        self.fuerza = random.randrange(5,10)
        self.inteligencia = random.randrange(2,5)
        self.vida = self.vida_max
        self.dano = self.dano_max
        self.habilidades = [Boomerang(), Golpear()]

    def __str__(self):

        return "Jugador2: " +str(self.nombre)+" Vida: "+str(self.vida)+"/"+str(self.vida_max)+" Dano: "+str(self.dano)+"/"+str(self.dano_max)

    def estadisticas(self):
        print(self.nombre)
        print("Vida:", self.vida, "/", self.vida_max)
        print("Dano", self.dano, "/", self.dano_max)
        print("Fuerza:", self.fuerza)
        print("Inteligencia:",self.inteligencia)

    def eleccion(self):
       x = random.randrange(1, 2)
       return x







		