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

UserName = ""
PassWord = ""
NomDuFichier = ""

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
input_Raison = Entry(gui, bd = 10)
input_Raison.pack()

##definir le Label Username
gui_UserName = StringVar()
label_UserName = Label(gui, textvariable=gui_UserName, relief=RAISED)
gui_UserName.set("Veuillez Entrer votre pseudo/Email ")
label_UserName.pack()

###Creation du widget input_UserName
input_UserName = Entry(gui, bd = 10 )
input_UserName.pack()

##definir le Label Nom du fichier de destination 
gui_NomDuFichier = StringVar()
label_NomDuFichier = Label(gui, textvariable=gui_NomDuFichier, relief=RAISED)
gui_NomDuFichier.set("Veuillez entrer le nom du fichier de destination")
label_NomDuFichier.pack()

###Creation du widget input_NomDuFichier
input_NomDuFichier = Entry(gui, bd = 10 )
input_NomDuFichier.pack()

#Creation du bouton Valider les donnees 
def btn_Entrer_Validation():
	
	#### Recuperer la donnee Raison
    Raison = input_Raison.get()
    #### Recuperer la donnee UserName
    UserName = input_UserName.get()
    #### Recuperer la donnee NomDuFichier
    NomDuFichier = input_NomDuFichier.get()
 
    print(Raison, UserName, NomDuFichier)

    Raison = Raison.lower()
    i = 0
    Longueur = 13
    PassWord = ""

    while ( i != Longueur):
            i+=1
            x=randint(0,62)
            PassWord = PassWord + Matrice[x]

    chdir("/home/rouboufi/Desktop")
    obFichier = open(NomDuFichier,'a')
    obFichier.write("Nom de l\'application : %s\n Nom d\'utilisateur : %s \n Mots de passe : %s \n" % (Raison, UserName, PassWord)) 
    obFichier.close()
    messagebox.showinfo("Le mot de passe a ete creer")

btn_Entrer = tkinter.Button(gui,text = "Entrer", command = btn_Entrer_Validation)
NomDuFichier = input_NomDuFichier.get()
UserName = input_UserName.get()
Raison = input_Raison.get()

btn_Entrer.pack()

gui.mainloop()
