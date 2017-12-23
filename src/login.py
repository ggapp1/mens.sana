import hashlib
import getpass
import os
import mysql.connector
from time import sleep
import diary



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
            if(new_user == "g"):
                diary.run("ggapp")
            else:
        		login = raw_input("	Digite o login: ")
        		password = getpass.getpass("	Digite a senha: ")

        		if authLogin(login,password):
        			activeUser = login
        			diary.run(activeUser)
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
