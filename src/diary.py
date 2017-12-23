import os
import mysql.connector
from datetime import datetime
import hashlib
import getpass
from time import sleep


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
	os.system("clear")
	print("################################################################################")
	print("############################## ENTRIES BY DATE #################################")
	print("################################################################################")
	print "\n\n"
	date = raw_input("	Digite a data (YYYY-MM-DD): ")
	connection = mysql.connector.connect(user='root', password='root', host='127.0.0.1', database='menssana')
	cursor = connection.cursor()

	query=('SELECT title,text,date(creation_date),time(creation_date) FROM entry where date(creation_date) = %s')
	query2=('SELECT count(*) FROM entry where date(creation_date) = %s')
	cursor.execute(query2, (date,))
	for i in cursor:
		print "\nForam encontrados "+str(i[0])+" registros nessa data!"
	b = raw_input("Aperte uma tecla para ver as entradas: ")
	cursor.execute(query, (date,))
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
	new_user = raw_input("Aperte enter para logar: ")
	print("\n\n")
	if(new_user == "y"):
		login = raw_input("	Digite novo login: ")
		password = getpass.getpass("	Digite a nova senha: ")
		createUser(login, password)
		print("usuario criado")
		logon()
	else:
		login = raw_input("	Digite o login: ")
		password = getpass.getpass("	Digite a senha: ")

		if authLogin(login,password):
			run()
		else:
			print("usuario ou senha incorreta")
			sleep(5)
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

def createUser(login, password):
	connection = mysql.connector.connect(user='root', password='root', host='127.0.0.1', database='menssana')
	cursor = connection.cursor()

	insert_user = ('INSERT INTO user (login, password) VALUES (%s, %s)')
	user_data = (login, hashlib.md5(password).hexdigest())

	cursor.execute(insert_user, user_data)
	connection.commit()
	cursor.close()
	connection.close()

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
		print("	3 - Consultar registros por data")

		print("	0 - Sair")
		option = int(raw_input())
		if option == 1:
			readNewEntry()
		elif option == 2:
			seeAllEntries()
		elif option == 3:
			consultEntry()
		elif option == 0:
			running = False
		else:
			print "Codigo invalido!"
