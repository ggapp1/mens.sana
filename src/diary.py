import os
import mysql.connector
from datetime import datetime


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
	
	confirm = (raw_input("\nInserir entrada?"))
	
	if(confirm == '1'):
		saveEntry(DiaryEntry(title,entry))
		raw_input("Insercao bem sucedida!\nPressione uma tecla para voltar ao menu")
	else:
		readNewEntry()


def consultEntry():
	print "o"
def seeEntries():
	print "s"

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
		print("	2 - Consultar um registro por data")
		print("	3 - Verificar a quantidade de registros, por data")
		print("	4 - Sair")
		option = int(raw_input())
		if option == 1:
			readNewEntry()
		elif option == 2:
			consultEntry()
		elif option == 3:
			seeEntries()
		elif option == 4:
			running = False
		else:
			print "Codigo invalido!"
