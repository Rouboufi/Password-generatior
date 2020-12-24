# -*- coding: utf-8 -*-
# Createur <rouboufi>
# Python Script 
# Start

from random import randint
from os import chdir
from time import strftime
import tkinter
from tkinter import *
from tkinter import messagebox 

temp=strftime('#\t\t\t %d/%B/%Y\t%H:%M:%S\t\t\t\t#')
Raison = 0
UserName = ""
Longueur=13
PassWord = ""
NomDuFichier = ""
i=0
Matrice = '1234567890qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'

###Creation de l'interface graphique
gui = Tk()

#definir la taille de l'interface graphique
gui.geometry("400x300")

##definir le Label Raison 
gui_Raison = StringVar()
label_Raison = Label(gui, textvariable=gui_Raison, relief=RAISED)

gui_Raison.set("Veuillez entrer le nom de l'application")
label_Raison.pack()

###Creation du widget input_Raison
input_Raison = StringVar() 
input_Raison = Entry(gui, bd = 10)
input_Raison.pack()

#### Recuperer la donnee Raison

Raison = input_Raison.get()

##definir le Label Username
gui_UserName = StringVar()
label_UserName = Label(gui, textvariable=gui_UserName, relief=RAISED)

gui_UserName.set("Veuillez Entrer votre pseudo/Email ")
label_UserName.pack()

###Creation du widget input_UserName
input_UserName = StringVar() 
input_UserName = Entry(gui, bd = 10 )
input_UserName.pack()

#### Recuperer la donnee UserName

UserName = input_UserName.get()


##definir le Label Nom du fichier de destination 
gui_NomDuFichier = StringVar()
label_NomDuFichier = Label(gui, textvariable=gui_NomDuFichier, relief=RAISED)

gui_NomDuFichier.set("Veuillez entrer le nom du fichier de destination")
label_NomDuFichier.pack()

###Creation du widget input_NomDuFichier
input_NomDuFichier = StringVar() 
input_NomDuFichier = Entry(gui, bd = 10 )
input_NomDuFichier.pack()

#### Recuperer la donnee NomDuFichier

NomDuFichier = input_NomDuFichier.get()


#Creation du bouton Valider les donnees 
def btn_Entrer_Validation():
	messagebox.showinfo("Le mot de passe a ete creer")

btn_Entrer = tkinter.Button(gui, text ="Entrer", command = btn_Entrer_Validation)
NomDuFichier = input_NomDuFichier.get()
UserName = input_UserName.get()
Raison = input_Raison.get()

btn_Entrer.pack()



while True :

	gui.mainloop()
	str = Raison
	Raison = Raison.lower()

	Longueur = int(Longueur)

	while ( i != Longueur):
			i+=1
			x=randint(0,62)
			PassWord = PassWord + Matrice[x]

	print("\n\n\nLe mot de passe va être écrit dans le fichier /home/USER/Bureau/%s" % NomDuFichier)

	chdir("/home/rouboufi/Desktop")

	obFichier = open('file:///home/rouboufi/Desktop/NomDuFichier')

	obFichier.write("Nom de l\'application : %s\n Nom d\'utilisateur : %s \n Mots de passe : %s \n" % (Raison, UserName, PassWord)) 

	obFichier.close()
gui.mainloop()
