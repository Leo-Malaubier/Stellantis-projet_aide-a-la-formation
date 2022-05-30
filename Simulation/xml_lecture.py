#!/usr/bin/env python

# -*- coding: utf-8 -*-

from tkinter import *
from lxml import etree
import logging

import Simulation.boutton_valeur
import Simulation.Erreur
import GenXml.Accueil
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

class Lecture(Frame):
    logger = logging.getLogger()
    NomCLASS ="Simulation"
    def __init__(self,pere):
        self.logger.info("--------xml_lecture-----------")
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

        self.logger.debug((self.lecture,"lecture"))
        self.logger.debug((self.lecture.split(".")[1],"lecture avec split"))

        emplacement_fichier_xml="../../fichier_cours/xml/"

        if self.lecture.split(".")[1]== "xlsx" or self.lecture.split(".")[1]=="csv":
            self.logger.info('----recherche de lecture xml-------------')
            self.lecture=emplacement_fichier_xml+ligne[1].split(".")[0]+".xml"
        else:
            self.lecture=emplacement_fichier_xml+ligne[1]
        self.affichage()
        self.organisation(None)

        self["background"]="#9D6ED2"
        self["width"]=self._pere.winfo_width()
        self["height"]=self._pere.winfo_height()
        self.pack_propagate(False)
        self.pack(side=BOTTOM,fill=None, expand=False)


    def retour(self):
        self._pere.switch(GenXml.Accueil.Connexion)

    def refresh(self):
        self.organisation("modif")
        #pour les assenseur il faut des canvas (voir scrollregion)(idée abandonée)

    def affichage(self):
        self.logger.info("---- affichage -----")
        self.logger.info((self._pere.winfo_width(),'information parent width: '))
        self.logger.info((self._pere.winfo_height(),'information parent height: '))

        self.frame1=LabelFrame(self,bg="brown",width=self._pere.winfo_width(),height=(self._pere.winfo_height()/3),text="frame1")
        self.frame2=LabelFrame(self,bg="green",width=self._pere.winfo_width(),height=(self._pere.winfo_height()/3),text="frame2")
        self.frame3=LabelFrame(self,bg="yellow",width=self._pere.winfo_width(),height=(self._pere.winfo_height()/3),text="frame3")
        Button(self.frame2, text="actualise",command = self.refresh).pack()
        Button(self.frame2, text="retour",command = self.retour).pack()
        Button(self.frame2, text="print",command = self.calcule_points).pack()
        self.liste_label_frame_pere=[]
        self.liste_boutton=[]
        self.logger.debug((self.lecture,"lecture du fichier (normalement xml)"))
        document = etree.parse(self.lecture)
        for pere in document.xpath("/Famille/Pere"):
            self.logger.debug(pere.get("name"))
            self.logger.debug(len(pere))

            self.liste_label_frame_pere.append(LabelFrame(self.frame3,relief=RAISED,text=pere.get("name"))) #création des label_fram pere
            #liste_label_frame_pere apprend des LabelFrame nomé au nom du père, appartenant au labelframe self.frame3

            liste_temp_boutton=[]
            for i in range(len(pere)):
                fils=pere[i].get("name")
                #création d'un bouton avec pour paramètre sont père (les freame que l'on a créer et mis en liste)
                liste_temp_boutton.append(Simulation.boutton_valeur.Valeur(self.liste_label_frame_pere[len(self.liste_label_frame_pere)-1]))
                liste_temp_boutton[i].set_nom(fils)
                self.logger.info("fils")
                self.logger.info(fils)#nom fils

            self.liste_boutton.append(liste_temp_boutton)
            #liste d'objet boutton_valeur ou chaque objet a pour paramètre initiale sont père (une labelframe contenue dans une labelframe)
        #on a donc 3 frame (frame1,frame2,frame3)
        #qui contienne un nombre de labelframe (selon le nombre de père trouvé dans le xml)
        #cette liste est stocké dans liste_label_frame_pere
        #une liste (liste_boutton) d'objet boutton_valeur qui on pour parent un élément de la liste liste_label_frame_pere
        #la liste de boutton est sous un forme simulaire à: [[],[]]


    def organisation(self,modif):
        self.logger.debug('--------------------------------------')
        self.logger.debug(self.liste_boutton)
        max=self.max_boutton_ligne()
        for i in range(len(self.liste_boutton)):
            collone=0
            ligne=0
            self.logger.debug(self.liste_boutton)
            self.logger.debug(len(self.liste_boutton))
            for j in range(len(self.liste_boutton[i])):
                if j%max==0:
                    collone=0
                    ligne+=1
                else:
                    collone+=1

                self.liste_boutton[i][j]._l=ligne
                self.liste_boutton[i][j]._c=collone
                if modif==None:
                    self.logger.debug(self.liste_boutton[i][j])
                    self.liste_boutton[i][j].creation(i)
                else:
                    self.liste_boutton[i][j].position()
        if modif==None:
            self.grid_pack()



    def grid_pack(self):#position chaque fram
        for i in range(len(self.liste_label_frame_pere)):
            self.liste_label_frame_pere[i].grid(column=i,row=0)
            self.logger.info(self.liste_label_frame_pere[i])# "est paqué"

        self.frame1.grid_propagate(False)
        self.frame1.pack_propagate(False)
        self.frame1.pack(side=TOP,fill=None, expand=False)

        self.frame2.grid_propagate(False)
        self.frame2.pack_propagate(False)
        self.frame2.pack(side=TOP,fill=None, expand=False)

        self.frame3.grid_propagate(False)
        self.frame3.pack_propagate(False)
        self.frame3.pack(side=BOTTOM,fill=None, expand=False)

    def max_boutton_ligne(self):
        largeur=self._pere.winfo_width()

        self.logger.info((largeur,"ici la largeur"))
        #pas besoin de prendre le PAD et le DIM de chacun vu qu'il on tous le même
        PAD=self.liste_boutton[0][0].PAD
        DIM=self.liste_boutton[0][0].DIM
        Nboutton=len(self.liste_boutton)

        self.logger.info(Nboutton)#"ici Nboutton"
        self.logger.info((PAD,"ici PAD "))
        self.logger.info((DIM,"ici DIM"))
        self.logger.info(int((largeur/Nboutton)//(PAD+DIM)))#calcule nombre de boutton par ligne

        return int(((largeur/Nboutton)//(PAD+DIM)))




    def calcule_points(self):
        document = etree.parse(self.lecture)
        for i in range(len(self.liste_boutton)):
            for j in range(len(self.liste_boutton[i])):
                parent=self.liste_boutton[i][j]._parent['text']
                nom=self.liste_boutton[i][j]._nom
                value=self.liste_boutton[i][j]._value

                self.logger.info("information parent nom value type(value) pour les erreurs")
                self.logger.info(parent)
                self.logger.info(nom)
                self.logger.info(value)
                self.logger.info(type(value))

                self.trouve_pere(parent,value)

    def trouve_pere(self,parent,value):
        document = etree.parse(self.lecture)
        for pere in document.xpath("/Famille/Pere"):
            #print("voila le père:",pere.get("name"))
            #print("voila le père envoyé:",parent)
            if pere.get("name") == parent:
                for i in range(len(pere)):
                    #print(pere[i].get("name"))
                    for j in range(len(pere[i])):
                        self.logger.info("-----------information détaillé-------------")
                        self.logger.info(("id: ",pere[i][j].get("id")))
                        self.logger.info(type(pere[i][j].get("id")))
                        self.logger.info(("value :",value))
                        self.logger.info(("petit_fils :",pere[i][j]))
                        if pere[i][j].get("id") == str(value):
                            self.logger.debug("------------------------")
                            self.logger.debug(pere[i][j].get("couleur"))
                            self.logger.debug(pere[i][j].get("titre_1"))
                            Liste_Titre=[]
                            Liste_erreur=[]
                            val=True
                            var=0
                            self.logger.debug(type(pere[i][j].get('titre_'+str(var))),"voici un type")
                            while (val==True):
                                if isinstance(pere[i][j].get('titre_'+str(var)),str) == True :
                                    if pere[i][j].get('titre_'+str(var)) != "None":
                                        self.logger.debug(pere[i][j].get('titre_'+str(var)), "-----------------------titre--------------------------------")
                                        self.logger.debug(type(pere[i][j].get('titre_'+str(var))))
                                        self.logger.debug("+1")
                                        var+=1
                                    else:
                                        val=False
                                        self.logger.debug("stop")
                                else:
                                    val=False
                                    self.logger.debug("stop")

                            val=True
                            var=0
                            while (val==True):
                                if isinstance(pere[i][j].get('commentaire_'+str(var)),str) == True :
                                    if pere[i][j].get('commentaire_'+str(var)) != "None":
                                        self.logger.debug(pere[i][j].get('commentaire_'+str(var)), "-----------------------commentaire--------------------------------")
                                        self.logger.debug(type(pere[i][j].get('commentaire_'+str(var))))
                                        self.logger.debug("+1")
                                        var+=1
                                    else:
                                        val=False
                                        self.logger.debug("stop")
                                else:
                                    val=False
                                    self.logger.debug("stop")
