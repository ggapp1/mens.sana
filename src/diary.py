import os
import mysql.connector
from datetime import datetime
import hashlib
import getpass


class DiaryEntry:
	def __init__(self, title, text):
		self.title = title
		self.text = text

def saveEntry(entry):

	connection = mysql.connector.connect(user='root', password='root', host='127.0.0.1', database='menssana')
	

	cursor = connection.cursor()

	insert_entry = ('INSERT INTO entry (title, text) VALUES (%s, %s)')
	entry_data = (entry.title, entry.text)

	cursor.execute(insert_entry, entry_data)
	connection.commit()
	cursor.close()
	connection.close()


def readNewEntry():
	os.system("clear")
	print("################################################################################")
	print("############################ INSERIR NOVA ENTRADA ##############################")
	print("################################################################################")
	title = raw_input("	Digite o titulo (opcional): ")
	entry = raw_input("	Digite a entrada: ")
	print("\nEntrada a ser inserida: \n")
	print "	"+title
	print "\n	"+entry
	
	confirm = (raw_input("\nInserir entrada? (Digite 1 para confirmar) "))
	
	if(confirm == '1'):
		saveEntry(DiaryEntry(title,entry))
		raw_input("Insercao bem sucedida!\nPressione uma tecla para voltar ao menu: ")
	else:
		readNewEntry()


def consultEntry():
	date = raw_input("	Digite a data: ")

def seeEntries():
	print "s"

def seeAllEntries():
	connection = mysql.connector.connect(user='root', password='root', host='127.0.0.1', database='menssana')
	cursor = connection.cursor()

	query = ('SELECT title, text, date(creation_date), time(creation_date) FROM entry')
	
	cursor.execute(query)
	for title, text, date, time in cursor:
		os.system("clear")
		print("################################################################################")
		print("################################ ALL ENTRIES ###################################")
		print("################################################################################")
		print "\n\n"
		print(title + ", as " + str(time) + ", em " + str(date) + ".")
		print "	"+text
		b = raw_input("\n\nAperte uma tecla para ir para a proxima entrada: ")
	c = raw_input("Fim das entradas, aperte uma tecla para voltar ao menu: ")	

	cursor.close()
	connection.close()

def logon():
	os.system("clear")
	print("################################################################################")
	print("################################# WELCOME TO ###################################")
	print("#################################  MENS SANA ###################################")
	print("################################################################################")
	print("\n\n")
	login = raw_input("	Digite o login: ")
	password = getpass.getpass("	Digite a senha: ")

	if authLogin(login,password):
		run()
	else:
		logon()

def authLogin(login, password):
	connection = mysql.connector.connect(user='root', password='root', host='127.0.0.1', database='menssana')
	
	logged = False
	cursor = connection.cursor()

	query = ('SELECT password FROM user WHERE login = %s')

	cursor.execute(query, (login,))
	for p in cursor:
		if hashlib.md5(password).hexdigest() == p[0]:
			logged = True

	cursor.close()
	connection.close()
	return logged


def run():
	
	running = True
	while running:
		os.system("clear")
		print("################################################################################")
		print("################################# WELCOME TO ###################################")
		print("#################################  MENS SANA ###################################")
		print("################################################################################")
		print("Escolha uma opcao:")
		print("	1 - Criar novo registro")
		print("	2 - Consultar todos os registros")
		print("	3 - Verificar a quantidade de registros, por data")
		print("	4 - Consultar um registro por data")
		print("	5 - Sair")
		option = int(raw_input())
		if option == 1:
			readNewEntry()
		elif option == 2:
			seeAllEntries()
		elif option == 3:
			seeEntries()
		elif option == 4:
			rconsultEntry()
		elif option == 5:
			running = False
		else:
			print "Codigo invalido!"
