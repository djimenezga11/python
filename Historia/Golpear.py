import random

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
			
            
        