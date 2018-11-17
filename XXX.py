from random import choice
from pyknow import *


class Juego(Fact): 
	""" Juegos que se pueden escoger"""
	pass

class Dinero(Fact):
	"""Dinero disponible que se tiene"""
	pass
Lista =['Juego1','Juego2']
Dinero =['Muy poco','Poco','Normal','Mucho','No es un problema']

class ConjuntoPCs(KnowledgeEngine):
	@Rule(AND(Juego(VJuego='Juego1'),Dinero(VDinero='Muy poco')))
	def the_user_has_power(self):
		ListaPC=['Alienware 15','Alienware 17']
		print(ListaPC)

        
	@Rule(AND(Juego(VJuego='Juego2'),Dinero(VDinero='Muy poco')))
	def the_user_has(self):
		print("El juego es Starcraft2")

engine = ConjuntoPCs()
engine.reset()
engine.declare(Juego(VJuego = choice(Lista)))
engine.declare(Dinero(VDinero = choice(Dinero)))
engine.run()

engine.declare(Juego(VJuego = choice(ListaJuego)))
engine.declare(Dinero(VDinero = choice(ListaDinero)))