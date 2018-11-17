#!/usr/bin/env python
# coding: utf-8

# In[90]:


from random import choice
from pyknow import *


# In[91]:


class Juego(Fact): 
	""" Juegos que se pueden escoger"""
	pass

class Dinero(Fact):
	"""Dinero disponible que se tiene"""
	pass
ListaJuego =['Juego1','Juego2','Juego3','Juego4','Juego5']
ListaDinero =['Poco','Normal','Mucho']
     
def ObtenerElMayor(x):
	mayor = 0
	for valor in x:
		if mayor < valor:
			mayor = valor
	if mayor == 7000:
		return 'Juego1'
	if mayor == 3000:
		return 'Juego2'
	if mayor == 7500:
		return 'Juego3'
	if mayor == 4500:
		return 'Juego4'
	if mayor == 6000:
		return 'Juego5'

# In[102]:


class ConjuntoPCs(KnowledgeEngine):
	ListaPC=[]
	def ReturnLista(self):
		return self.ListaPC
	@Rule(AND(OR(Juego(VJuego='Juego1'),Juego(VJuego='Juego3')),Dinero(VDinero='Poco')))
	def JPP_D(self):
		self.ListaPC=['IdealPad 330','Legion Y520','Serie X570UB']


	@Rule(AND(OR(Juego(VJuego='Juego1'),Juego(VJuego='Juego3')),Dinero(VDinero='Normal')))
	def JPN_D(self):
		self.ListaPC=['HP Omen 17','Dell G5','Asus FX504GD-DM328T']
        
	@Rule(AND(OR(Juego(VJuego='Juego1'),Juego(VJuego='Juego3')),Dinero(VDinero='Mucho')))
	def JPM_D(self):
		self.ListaPC=['MSI GT5 TITAN8RG','ROG Zephyrus M (GM501)','Alienware 15']
        
	@Rule(AND(Juego(VJuego='Juego5'),Dinero(VDinero='Poco')))
	def JNP_D(self):
		self.ListaPC=['IdealPad 330','K555LB-XX131H', 'X540UV']
        
	@Rule(AND(Juego(VJuego='Juego5'),Dinero(VDinero='Normal')))
	def JNN_D(self):
		self.ListaPC=['Dell G5','Legion Y520','Serie X570UB']
        
	@Rule(AND(Juego(VJuego='Juego5'),Dinero(VDinero='Mucho')))
	def JNM_D(self):
		self.ListaPC=['Alienware 15','Asus FX504GD-DM328T','HP Omen 17']

	@Rule(AND(OR(Juego(VJuego='Juego2'),Juego(VJuego='Juego4')),Dinero(VDinero='Poco')))
	def JLP_D(self):
		self.ListaPC=['Hp AM15','Dell PG', 'X440UV']
        
	@Rule(AND(OR(Juego(VJuego='Juego2'),Juego(VJuego='Juego4')),Dinero(VDinero='Normal')))
	def JLN_D(self):
		self.ListaPC=['K555LB-XX131H','X540UV',' Asus DGR120']
        
	@Rule(AND(OR(Juego(VJuego='Juego2'),Juego(VJuego='Juego4')),Dinero(VDinero='Mucho')))
	def JLM_D(self):
		self.ListaPC = ['Dell G5','Serie X570UB', 'IdealPad 330']
    

    


# In[105]:


def LogicaProposicional(x,y):
	OPJuego = ObtenerElMayor(x)
	engine = ConjuntoPCs()
	engine.reset()
	engine.declare(Juego(VJuego = OPJuego))
	engine.declare(Dinero(VDinero = y))
	engine.run()
	return engine.ReturnLista()
   