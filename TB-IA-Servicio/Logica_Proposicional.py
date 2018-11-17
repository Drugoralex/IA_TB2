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
     


# In[102]:


class ConjuntoPCs(KnowledgeEngine):
	ListaPC = []
	def ReturnLista(self):
		return self.ListaPC
	@Rule(AND(OR(Juego(VJuego='Juego1'),Juego(VJuego='Juego3')),Dinero(VDinero='Poco')))
	def JPP_D(self):
		self.ListaPC=['Alienware 15','Alienware 17']


	@Rule(AND(OR(Juego(VJuego='Juego1'),Juego(VJuego='Juego3')),Dinero(VDinero='Normal')))
	def JPN_D(self):
		self.ListaPC=['Alienware 15','Alienware 17']
        
	@Rule(AND(OR(Juego(VJuego='Juego1'),Juego(VJuego='Juego3')),Dinero(VDinero='Mucho')))
	def JPM_D(self):
		self.ListaPC=['Alienware 15','Alienware 17']
        
	@Rule(AND(Juego(VJuego='Juego5'),Dinero(VDinero='Poco')))
	def JNP_D(self):
		self.ListaPC=['Alienware 15','Alienware 17']
        
	@Rule(AND(Juego(VJuego='Juego5'),Dinero(VDinero='Normal')))
	def JNN_D(self):
		self.ListaPC=['Daniel Aragon','Alienware 17']
        
	@Rule(AND(Juego(VJuego='Juego5'),Dinero(VDinero='Mucho')))
	def JNM_D(self):
		self.ListaPC=['Alienware 15','Alienware 17']

	@Rule(AND(OR(Juego(VJuego='Juego2'),Juego(VJuego='Juego4')),Dinero(VDinero='Poco')))
	def JLP_D(self):
		self.ListaPC=['Alienware 15','Alienware 17']
        
	@Rule(AND(OR(Juego(VJuego='Juego2'),Juego(VJuego='Juego4')),Dinero(VDinero='Normal')))
	def JLN_D(self):
		self.ListaPC=['Alienware @de','Alienware 17']
        
	@Rule(AND(OR(Juego(VJuego='Juego2'),Juego(VJuego='Juego4')),Dinero(VDinero='Mucho')))
	def JLM_D(self):
		self.ListaPC = ['Alienware 15','Alienware 17']
    


# In[105]:


def LogicaProposicional(x,y):
    engine = ConjuntoPCs()
    engine.reset()
    engine.declare(Juego(VJuego = x))
    engine.declare(Dinero(VDinero = y))
    engine.run()
    return engine.ReturnLista()
   

 




