#!/usr/bin/python3
import random
import pickle
import operator
import datetime
__author__ = 'marcelo'
arquivo = 'dados.dat'

class Participante:

	def __init__(self,nome,telefone='',email=''):
		self.setNome(nome)
		self.setTelefone(telefone)
		self.setEmail(email)
		self.dataCadastro = datetime.datetime.now().strftime("%d-%m-%Y")

	def setNome(self,nome):
		if nome.strip():
			self.nome =  " ".join(nome.split()).title()
		else:
			raise TypeError('Nome não pode ser vazio')

	def setTelefone(self,telefone):
		if telefone == None:
			self.telefone = ''
		else:
			self.telefone = telefone

	def setEmail(self,email):
		if email == None:
			self.email = ''
		else:
			self.email = email.lower()

	def getNome(self):
		return self.nome

	def getTelefone(self):
		return self.telefone

	def getEmail(self):
		return self.email

	def getDataCadastro(self):
		return self.dataCadastro

	def eIgual(self,nome):
		nome = " ".join(nome.split()).title()
		if nome == self.nome:
			return True
		else:
			return False

def adicionar(participante):
	participantes = getParticipantes()
	participantes.append(participante)
	with open(arquivo,'wb') as arq_file:
		pickle.dump(participantes,arq_file)

def sortear():
	participantes = getParticipantes()
	if len(participantes) == 0:
		return -1
	else:
		return random.choice(participantes)

def remover(nome):
	participantes = getParticipantes()
	for participante in participantes:
		if(participante.eIgual(nome)):
			participantes.remove(participante)
			with open(arquivo,'wb') as arq_file:
				pickle.dump(participantes,arq_file)
			return 0
	return -1

def limpar():
	listaVazia = list()
	with open(arquivo,'wb') as arq_file:
		pickle.dump(listaVazia,arq_file)

def getParticipantes():
	try:
		with open(arquivo,'rb') as arq_file:
			participantes = pickle.load(arq_file)
	except IOError as err:
		participantes = list()
	return participantes




