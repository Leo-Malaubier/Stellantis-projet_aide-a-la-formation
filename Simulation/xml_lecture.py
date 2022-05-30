#!/usr/bin/env python

# -*- coding: utf-8 -*-

from tkinter import *
from lxml import etree
import Simulation.boutton_valeur
import Simulation.Erreur
import GenXml.Accueil
class Lecture(Frame):
    NomCLASS ="Simulation"
    def __init__(self,pere):
        self._pere=pere
        Frame.__init__(self, pere)


        self.boutton=Simulation.boutton_valeur.Valeur(self._pere)
        self.boutton.pack()

        file=open("temp/temporaire.txt","r")
        ligne=file.readlines(0)


        #lien complet du fichier(/!\ il peux y avoir un \n)
        try:
            self.lecture=ligne[1].split('\n')[0]
        except:
            self.lecture=ligne[1]

        print(self.lecture)
        print(self.lecture.split(".")[1])



        if self.lecture.split(".")[1]== "xlsx" or self.lecture.split(".")[1]=="csv":
            print('----recherche de lecture xml-------------')
            self.lecture="../../fichier_cours/xml/"+ligne[1].split(".")[0]+".xml"
        else:
            self.lecture="../../fichier_cours/xml/"+ligne[1]
        Button(self, text="actualise",command = self.refresh).pack()
        Button(self, text="retour",command = self.retour).pack()
        self.affichage()
        self.organisation(None)

    def retour(self):
        self.destroy()
        self._pere.switch(GenXml.Accueil.Connexion)

    def refresh(self):
        self.organisation("modif")
        #pour les assenseur il faut des canvas (voir scrollregion)

    def affichage(self):
        self.frame1=Frame(self,bg="brown")
        self.frame2=Frame(self,bg="green")
        self.frame3=Frame(self,bg="#FFFFFF")

        self.liste_label_frame_pere=[]
        self.liste_boutton=[]
        print(self.lecture,"lecture du fichier (normalement xml)")
        document = etree.parse(self.lecture)
        for pere in document.xpath("/Famille/Pere"):
            #print(pere.get("name"))
            #print(len(pere))

            self.liste_label_frame_pere.append(LabelFrame(self.frame3,relief=RAISED,text=pere.get("name"))) #création des label_fram pere
            liste_temp_boutton=[]
            for i in range(len(pere)):
                fils=pere[i].get("name")
                #création d'un bouton avec pour paramètre sont père (les freame que l'on a créer et mis en liste)
                liste_temp_boutton.append(Simulation.boutton_valeur.Valeur(self.liste_label_frame_pere[len(self.liste_label_frame_pere)-1]))
                print(fils)#nom fils

            self.liste_boutton.append(liste_temp_boutton)


    def organisation(self,modif):
        print('--------------------------------------')
        print(self.liste_boutton)
        max=self.max_boutton_ligne()
        for i in range(len(self.liste_boutton)):
            collone=0
            ligne=0
            print(self.liste_boutton)
            print(len(self.liste_boutton))
            for j in range(len(self.liste_boutton[i])):
                if j%max==0:
                    collone=0
                    ligne+=1
                else:
                    collone+=1

                self.liste_boutton[i][j]._l=ligne
                self.liste_boutton[i][j]._c=collone
                if modif==None:
                    print(self.liste_boutton[i][j])
                    self.liste_boutton[i][j].creation(str(i))
                else:
                    self.liste_boutton[i][j].position()
        if modif==None:
            self.grid_pack()

    def grid_pack(self):#position chaque fram
        for i in range(len(self.liste_label_frame_pere)):
            self.liste_label_frame_pere[i].grid(column=i,row=0)
            print(self.liste_label_frame_pere[i], "est paqué")
        self.frame3.pack(side="bottom")

    def max_boutton_ligne(self):
        largeur=self._pere.winfo_width()
        print(largeur)
        PAD=self.liste_boutton[0][0].PAD
        DIM=self.liste_boutton[0][0].DIM
        Nboutton=len(self.liste_boutton)
        print(int((largeur/Nboutton)//(PAD+DIM)))#calcule nombre de boutton par ligne

        return int(((largeur/Nboutton)//(PAD+DIM)))

"""#recherche id petit_fils
for j in range(len(pere[i])):
    print(pere[i][j].get("id"))#id petit_fils /!\ l'id est de type str
    print(type(pere[i][j].get("id")))
    liste_label_frame_fils.append(Simulation.boutton_valeur.Valeur())
"""
