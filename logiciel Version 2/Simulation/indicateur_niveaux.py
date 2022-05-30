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

        Frame.__init__(self,master=self._parent)
        self.HEIGHT= pere.winfo_height()*3/4
        self.WIDTH=pere.winfo_width()*3/4
        self.Ncouleur=9
        # self._couleur_Positiv="#008000"#vert
        # self._couleur_moyenne="#FF7F00"#orange
        # self._couleur_negativ="#F00020"#rouge
        self._couleur_Positiv="green"#vert
        self._couleur_moyenne="orange"#orange
        self._couleur_negativ="red"#rouge
        self.epaisseur_trais=20
        self.jauge()
        self.cnv.pack()
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
                        self.cnv.create_arc(20,20,int(self.WIDTH)-20, int(self.HEIGHT)*1.5, extent=val, start=180-valeur-val, width=self.epaisseur_trais,style=ARC,outline=self._couleur_Positiv)
                        vert+=1
                    elif i >= orange:
                        self.cnv.create_arc(20,20,int(self.WIDTH)-20, int(self.HEIGHT)*1.5, extent=val, start=180-valeur-val, width=self.epaisseur_trais,style=ARC,outline=self._couleur_moyenne)
                    else:
                        self.cnv.create_arc(20,20,int(self.WIDTH)-20, int(self.HEIGHT)*1.5, extent=val, start=180-valeur-val, width=self.epaisseur_trais,style=ARC,outline=self._couleur_negativ)
                else:

                    if i <= rouge:
                        self.cnv.create_arc(20,20,int(self.WIDTH)-20, int(self.HEIGHT)*1.5, extent=val, start=180-valeur-val, width=self.epaisseur_trais,style=ARC,outline=self._couleur_moyenne)
                        print("orange")
                    else:
                        self.cnv.create_arc(20,20,int(self.WIDTH)-20, int(self.HEIGHT)*1.5, extent=val, start=180-valeur-val, width=self.epaisseur_trais,style=ARC,outline=self._couleur_negativ)
                        print("rouge")


#3 couleur = > rouge vert rouge
#5 couleur = > rouge orange vert orange rouge
#7 couleur = > rouge rouge orange vert orange rouge rouge
#9 couleur = > rouge rouge orange orange vert orange orange rouge
#soit obligatoirement un vert et un nombre orange forcément inférieur ou égale au rouge.
