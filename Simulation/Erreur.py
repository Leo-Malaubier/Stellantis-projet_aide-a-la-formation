#!/usr/bin/env python

# -*- coding: utf-8 -*-

from tkinter import *

class Erreur:

    def __init__(self,pere):
        self._couleur_erreur="#FFFFFF"
        self._nom_erreur=[]
        self._nom_parent=""
        self._commentaire=[]
        self._parent=pere
        self._c=0 #collone
        self._l=0#ligne

        self.bg_color="#FFFFFF"


    def affichage(self): #affichage les fonctions contenue dans affichage sont séparé de __init__ car l'on ne peux pas modifier les élément:
                         #self.label_frame et canvas une fois qu'ils sont affiché
        self.label_frame =LabelFrame(self._parent,width=100,height=50,bd=1,relief=RAISED,text=self._nom_parent,bg=self.bg_color)

        nom=""
        for i in range(len(self._nom_erreur)):
                nom+=self._nom_erreur[i]+"\n"

        self.label_frame_Fils=LabelFrame(self.label_frame,text=nom,bg=self.bg_color)
        canvas= Canvas(self.label_frame,bg=self._couleur_erreur,width=40,height=40)
        canvas.pack(side=LEFT)
        self.label_frame_Fils.pack(side=LEFT)

        for i in range(len(self._commentaire)):
            self._label=Label(self.label_frame_Fils,text=self._commentaire[i],bg=self.bg_color).pack()

    def placement(self):
        #print(self._c,self._l)
        self.label_frame.grid(column=self._c,row=self._l)


    def set_couleur_erreur(self,couleur): #prend un caractère
        self._couleur_erreur=couleur

    def set_erreur(self,nom):#prend une liste
        self._nom_erreur=nom

    def set_commentaire(self,commentaire):#prend une liste
        self._commentaire=commentaire

    def set_parent(self,nom):
        self._nom_parent=nom

    def get_taille(self): #la taille ne peux être aquise que si l'objet a été créer (avec la affichage)
        self.label_frame.update_idletasks()
        return self.label_frame.winfo_width()


#creation set a véritablement créer et mettre les information de l'erreur.
#la classe a cette forme car elle doit être amélioré pour que l'on puisse modifier l'affichage au lieux de créer les erreur puis les supprimer pour en refaire.
#voir si la méthode loop (mainloop) fonctionne correctement sur les éléments (il se peux que mainloop n'affecte pas correctement le widget, et de ce fait,
# l'objet erreur n'est pas actualisé si l'on change des paramètre comme la couleur ou le message)
#==> les problem vienne des focus. il fait définir les focus pour qu'il y es des modification.

    def creation(self,information):   #information = liste d'information en longueur=4 soit [0,1,2,3]
        self.set_couleur_erreur(information[0])#couleur
        print(information[0])
        self.set_erreur(information[1])#liste_erreur
        self.set_commentaire(information[2])#liste_commentaire
        self.set_parent(information[3])
        self.affichage()
"""
#exemple d'utilisation :
err=Erreur.Erreur(frame1)
err.creation(["yellow",["erreur","erreur seconde"],["commentaire1","commentaire2"],"parent"])
"""
