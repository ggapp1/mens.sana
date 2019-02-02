import os
import mysql.connector
from datetime import datetime
import login
import cipher

def connectDatabase():
	return mysql.connector.connect(user='root', password='', host='127.0.0.1', database='menssana')
	


class DiaryEntry:
	def __init__(self, title, text):
		self.title = title
		self.text = text

def saveEntry(entry, activeUser):

	connection = connectDatabase()
	cursor = connection.cursor()

	insert_entry = ('INSERT INTO entry (title, text, user) VALUES (%s, %s, %s)')
	entry_data = (entry.title, cipher.encrypt(activeUser,entry.text), activeUser)

	cursor.execute(insert_entry, entry_data)
	connection.commit()
	cursor.close()
	connection.close()

def newEntry(activeUser):
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
		saveEntry(DiaryEntry(title,entry), activeUser)
		raw_input("Insercao bem sucedida!\nPressione uma tecla para voltar ao menu: ")
	

def consultEntry(activeUser):
	os.system("clear")
	print("################################################################################")
	print("############################## ENTRIES BY DATE #################################")
	print("################################################################################")
	print "\n\n"

	date = raw_input("	Digite a data (YYYY-MM-DD): ")
	connection = connectDatabase()
	cursor = connection.cursor()

	query= 'SELECT title,text,date(creation_date),time(creation_date) ' \
		   'FROM entry where date(creation_date) = %s and user = %s'
	query2= 'SELECT count(*) FROM entry where date(creation_date) = %s and user = %s'
	cursor.execute(query2, (date,activeUser))
	for i in cursor:
		print "\nForam encontrados "+str(i[0])+" registros nessa data!"
	if(i[0] != 0):
		b = raw_input("Aperte uma tecla para ver as entradas: ")
		cursor.execute(query, (date,activeUser))
		for title, text, date, time in cursor:
			os.system("clear")
			print("################################################################################")
			print("################################ ALL ENTRIES ###################################")
			print("################################################################################")
			print "\n\n"
			print(title + ", as " + str(time) + ", em " + str(date) + ".")
			text = cipher.decrypt(activeUser, text)
			print "	"+text
			b = raw_input("\n\nAperte uma tecla para ir para a proxima entrada: ")
	c = raw_input("Fim das entradas, aperte uma tecla para voltar ao menu: ")

	cursor.close()
	connection.close()

def seeAllEntries(activeUser):
	connection = connectDatabase()
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
		text = cipher.decrypt(activeUser, text)
		print "	"+text
		b = raw_input("\n\nAperte uma tecla para ir para a proxima entrada: ")
	c = raw_input("Fim das entradas, aperte uma tecla para voltar ao menu: ")

	cursor.close()
	connection.close()

def run(user):
	running = True
	activeUser = user
	while running:
		os.system("clear")
		print activeUser
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
			newEntry(activeUser)
		elif option == 2:
			seeAllEntries(activeUser)
		elif option == 3:
			consultEntry(activeUser)
		elif option == 0:
			running = False
		else:
			print "Codigo invalido!"
