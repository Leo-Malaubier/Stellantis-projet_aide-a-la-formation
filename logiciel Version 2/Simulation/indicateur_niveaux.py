#!/usr/bin/env python

# -*- coding: utf-8 -*-

from tkinter import *
import math
import logging
import verififaction_file_log



fichier_log="log/log.log"

#--------------------------------------------------------------------------------------------
try:
    logging.basicConfig(filename=fichier_log, level=logging.DEBUG,
                            format='%(asctime)s - %(levelname)s:%(message)s')
except:
    verififaction_file_log.verification_file()
    logging.basicConfig(filename=fichier_log, level=logging.DEBUG,
                            format='%(asctime)s - %(levelname)s:%(message)s')
    logging.warning("les log n'existais pas et on été créer a partir de ajout_cours.py")

#--------------------------------------------------------------------------------------------



class indicateur_niveaux(Frame):
    logger = logging.getLogger()
    PAD=25 #marge pour que le cercle ne soit pas collé au bord du canvas
    DIM=80 #diamètre

    def __init__(self,pere):
        self.logger.info("--------indicateur_niveaux-----------")

        self._parent=pere #frame parente
        self._value=0

        Frame.__init__(self,master=self._parent)
        pere.update()
        self.HEIGHT= pere.winfo_height()*3/4
        self.WIDTH=pere.winfo_width()*3/4
        self.Ncouleur=5
        print(self.HEIGHT)
        print(self.WIDTH)
        # self._couleur_Positiv="#008000"#vert
        # self._couleur_moyenne="#FF7F00"#orange
        # self._couleur_negativ="#F00020"#rouge
        self._couleur_Positiv="green"#vert
        self._couleur_moyenne="orange"#orange
        self._couleur_negativ="red"#rouge
        self.epaisseur_trais=20
        self._value=0
        self.jauge()
        self.cnv.pack()
        #self.grid(row=0,column=1)
        self.pack()
    def jauge(self):
        self.cnv = Canvas(self, width=self.WIDTH, height=self.HEIGHT)

        val=180/self.Ncouleur
        position_vert=(self.Ncouleur//2)

        orange=position_vert//2

        rouge=position_vert+orange
        for i in range(self.Ncouleur):
            if self.Ncouleur == 3+(4*i):
                orange+=1
                break

        vert=0
        if self.Ncouleur%2 ==0:
            logger.warning("ATTENTION le nombre de couleur pour l'affichage doit être impaire supérieur ou égale a 3")
        else:
            for i in range(self.Ncouleur):
                valeur = i*val

                if vert==0:
                    if i == position_vert:
                        self.cnv.create_arc(20,20,int(self.WIDTH)-20, int(self.HEIGHT)*2, extent=val, start=180-valeur-val, width=self.epaisseur_trais,style=ARC,outline=self._couleur_Positiv)
                        print("vert")
                        vert+=1
                    elif i >= orange:
                        self.cnv.create_arc(20,20,int(self.WIDTH)-20, int(self.HEIGHT)*2, extent=val, start=180-valeur-val, width=self.epaisseur_trais,style=ARC,outline=self._couleur_moyenne)
                        print("orange")
                    else:
                        self.cnv.create_arc(20,20,int(self.WIDTH)-20, int(self.HEIGHT)*2, extent=val, start=180-valeur-val, width=self.epaisseur_trais,style=ARC,outline=self._couleur_negativ)
                        print("rouge")
                else:

                    if i <= rouge:
                        self.cnv.create_arc(20,20,int(self.WIDTH)-20, int(self.HEIGHT)*2, extent=val, start=180-valeur-val, width=self.epaisseur_trais,style=ARC,outline=self._couleur_moyenne)
                        print("orange")
                    else:
                        self.cnv.create_arc(20,20,int(self.WIDTH)-20, int(self.HEIGHT)*2, extent=val, start=180-valeur-val, width=self.epaisseur_trais,style=ARC,outline=self._couleur_negativ)
                        print("rouge")

        #= create_ligne fonctionne comme une droite avec 2 point au coordonées x,y . (soit 2 point donc x1,y1 et x2,y2)
        self.ligne=self.cnv.create_line(self.WIDTH/2,self.HEIGHT,self.HEIGHT-self.epaisseur_trais,self.HEIGHT-self.epaisseur_trais, width=4, fill="#000000")

    #les fonction ligne_modif, value_plus et value_moins sont récupéré de boutton_valeur
    def ligne_modif(self):
        R=self.HEIGHT-self.epaisseur_trais #rayon
        xC=self.WIDTH/2 #x
        yC=self.HEIGHT #y centre
        i=self._value
        if i!=0:
            angle_inter_element=180-180/(self.Ncouleur-1)*-i
            xMax=xC+R//1*math.cos(math.radians(angle_inter_element))#on prend le quotient du rayon //9 pour faire calculer une ligne
            yMax=yC+R//1*math.sin(math.radians(angle_inter_element))
            xMin=xC+R//4*math.cos(math.radians(angle_inter_element))#on prend le quotient du rayon //9 pour faire calculer une ligne
            yMin=yC+R//4*math.sin(math.radians(angle_inter_element))
            self.cnv.coords(self.ligne,xMax,yMax,xMin,yMin)
        else:#on évite la division et multiplication par 0
            xMax=xC+R//1*math.cos(math.radians(i+180))
            yMax=yC+R//1*math.sin(math.radians(i))
            xMin=xC+R//4*math.cos(math.radians(i+180))
            yMin=yC+R//4*math.sin(math.radians(i))
            self.cnv.coords(self.ligne,xMax,yMax,xMin,yMin)

    def value_plus(self):#position est l'endroit ou le clique a lieu. il n'est pas utile mais est retourné par le clique souris
        if self._value == self.Ncouleur-1: #-1 car l'on veux que la valeur 0 ou valeur initiale vale quelle que choses. soit 5valeurs et pas 5 (0,1,2,3,4,5)=6valeurs
            self._value=self._value
        else:
            self._value+=1
        self.ligne_modif()

    def value_moins(self):
        if self._value == 0:
            self._value=self._value
        else:
            self._value-=1
        self.ligne_modif()



#3 couleur = > rouge vert rouge
#5 couleur = > rouge orange vert orange rouge
#7 couleur = > rouge rouge orange vert orange rouge rouge
#9 couleur = > rouge rouge orange orange vert orange orange rouge
#soit obligatoirement un vert et un nombre orange forcément inférieur ou égale au rouge.
