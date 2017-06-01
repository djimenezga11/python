import random
import time

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


class Boomerang(object):
    def __init__(self):
        self.quita = 0
        self.nombre = "Boomerang"

    def devAtaque(self, origen):
        if origen.dano<10:
            return 0
        else:
            self.quita = random.randrange(11,16)+origen.inteligencia
            origen.dano += 10
            return self.quita

class Golpear(object):
	def __init__(self):
		self.quita = 0
		self.nombre = "Golpear"
		
	def devolverAtaque(self,origen):
		if origen.dano<5:
			return 0
		else:
			self.quita = random.randrange(12,16)+origen.fuerza
			origen.dano += -5
			return self.quita


def main():
    print("BIENVENIDO!!!\n----------------")
    nombre = input("Escribe tu nombre: ")
    nombre2 = input("El nombre de tu rival: ")
    j1 = Jugador(nombre)
    j2 = Jugador2(nombre2)
    print(" --------------------------")
    print("Jugador 1:")
    print(j1.estadisticas())
    print(" --------------------------")
    print(" --------------------------")
    print("Jugador 2:")
    print(j2.estadisticas())
    print(" --------------------------")
    time.sleep(5)
    
	    

    while j1.vida>0 and j2.vida>0:
        print("---------------")
        print(j1)
        print("---------------")
        print(j2)
        print("---------------")

        print("\nTURNO DE",j1.nombre)
        elec1 = j1.eleccion()
        j2.vida -=  j1.habilidades[elec1].devolverAtaque(j1)
        print("Has usado ",j1.habilidades[elec1].nombre)
        print("Atacando...")
        time.sleep(1)
        print("Daño",j1.habilidades[elec1].devolverAtaque(j1))
        time.sleep(0.5)
        if j1.vida<=0 and j2.vida<=0:
             break
		     
        print("\nTurno de",j2.nombre)
        elec2 = j2.eleccion()
        j1.vida -=  j2.habilidades[elec2].devolverAtaque(j2)
        print(j2.nombre,"ha usado ",j2.habilidades[elec2].nombre)
        print("Atacando...")
        time.sleep(1)
        print("Daño",j2.habilidades[elec2].devolverAtaque(j2))
        time.sleep(2)
        if j1.vida<=0 or j2.vida<=0:
            break 
        if j1.vida>0:
            print("Gana",j1.nombre)
        else:
            print("Gana",j2.nombre)
            	
main()


