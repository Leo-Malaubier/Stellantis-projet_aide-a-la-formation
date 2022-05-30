#!/usr/bin/env python

# -*- coding: utf-8 -*-

from tkinter import *
from lxml import etree
import logging

import Simulation.boutton_valeur
import Simulation.Erreur
import Simulation.indicateur_niveaux
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

        self.dictionnaire_indice={}
        self.disctionnaire_element={}

        self.parametres=GenXml.Lecture_Settings.settings()
        print(self.parametres._indice)

        self.boutton=Simulation.boutton_valeur.Valeur(self._pere)
        self.boutton.pack()

        file=open("temp/temporaire.txt","r")
        ligne=file.readlines(0)
        print(ligne)
        #lien complet du fichier(/!\ il peux y avoir un \n)
        try:
            self.lecture=ligne[1].split('\n')[0]
        except:
            self.lecture=ligne[1]

        try:
            self.chemain_complet_init=ligne[0].split('\n')[0]
        except:
            self.chemain_complet_init=ligne[0]
        #print("le chemain",self.chemain_complet_init)
        # print("voila le split", self.chemain_complet_init.split('.')[-1])
        # print(ligne[0].split('\n')[0])
        # print("ici",self.chemain_complet_init.split('.')[2])
        if  self.chemain_complet_init.split('.')[-1]== "xml":
            try:
                with open(self.chemain_complet_init.replace("xml","csv")): pass
                self.chemain_complet_init=self.chemain_complet_init.replace("xml","csv")

            except:
                try:
                    with open(self.chemain_complet_init.replace("xml","xlsx")): pass
                    self.chemain_complet_init=self.chemain_complet_init.replace("xml","xlsx")
                    self.logger.info("fichier trouvé")
                except:
                    self.logger.warning("fichier introuvable")
        else:
            self.logger.info("le fichier n'est pas xml")
        # print(self.chemain_complet_init)
        # print("voila le fichier",self.chemain_complet_init)
        self.logger.debug((self.lecture,"lecture"))
        self.logger.debug((self.lecture.split(".")[1],"lecture avec split"))

        emplacement_fichier_xml="../fichier_cours/xml/"

        if self.lecture.split(".")[1]== "xlsx" or self.lecture.split(".")[1]=="csv":
            self.logger.info('----recherche de lecture xml-------------')
            self.lecture=emplacement_fichier_xml+ligne[1].split(".")[0]+".xml"
        else:
            self.lecture=emplacement_fichier_xml+ligne[1]


        self.indice_element()

        self.affichage()
        self.organisation_bouton(None)


        self["background"]="#9D6ED2"
        self["width"]=self._pere.winfo_width()
        self["height"]=self._pere.winfo_height()
        self.pack_propagate(False)
        self.pack(side=BOTTOM,fill=None, expand=False)

        self.affichage_niveaux()
        self.affichage_fils_frame2()


    def indice_element(self):
        print("indice_element")
        NomSimple=self.chemain_complet_init.split('/')[-1]
        parametres=GenXml.Lecture_Settings.settings()
        if NomSimple.split('.')[-1] == 'csv':
            tableau_indice=GenXml.Lecture_Donnee.lecture_fueilles_csv(self.chemain_complet_init,parametres._indice)
        else:
            tableau_indice=GenXml.Lecture_Donnee.lecture_fueilles_xlsx(self.chemain_complet_init,parametres._indice)
        for i in range(len(tableau_indice)):
            if isinstance(tableau_indice[i][0],str):
                clef=""
                val=""
                for j in range(len(tableau_indice[i][0])):
                    if j == 0:
                        clef=tableau_indice[i][0][j]
                    else:
                        if tableau_indice[i][0][j]=="-" or tableau_indice[i][0][j]==">" or (tableau_indice[i][0][j]==" " and tableau_indice[i][0][j-1]==">" ) :
                            pass
                        else:
                            val+=tableau_indice[i][0][j]
                self.dictionnaire_indice[clef]=val

    def retour(self):
        self._pere.switch(GenXml.Accueil.Connexion)

    def refresh(self):
        self.organisation_bouton("modif") #permet de réorganisé les boutton si l'écran a changé de taille
        #pour les assenseur il faut des canvas (voir scrollregion)(idée abandonée)

    def affichage(self):
        self.logger.info("---- affichage -----")
        self.logger.info((self._pere.winfo_width(),'information parent width: '))
        self.logger.info((self._pere.winfo_height(),'information parent height: '))

        self.frame1=LabelFrame(self,width=self._pere.winfo_width(),height=(self._pere.winfo_height()/3),text="frame1")
        self.frame2=LabelFrame(self,width=self._pere.winfo_width(),height=(self._pere.winfo_height()/3),text="frame2")
        self.frame3=LabelFrame(self,width=self._pere.winfo_width(),height=(self._pere.winfo_height()/3),text="frame3")

        # Button(self.frame1, text="actualise",command = self.refresh).pack(side=LEFT)
        Button(self.frame1, text="retour",command = self.retour).grid(row=0,column=0)

        # Button(self.frame1, text="plus",command = self.plus).pack(side=LEFT)
        # Button(self.frame1, text="moins",command = self.moins).pack(side=LEFT)
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


    def affichage_fils_frame2(self):
        self.frame2.update()
        self.frame2.update_idletasks()
        print("ici",self.frame2.winfo_height())
        self.frame_image=       LabelFrame(self.frame2,width=(self.frame2.winfo_width()/3),height=self.frame2.winfo_height(),text="image")
        self.frame_commentaire= LabelFrame(self.frame2,width=(self.frame2.winfo_width()/3),height=self.frame2.winfo_height(),text="commentaire")
        self.frame_video=       LabelFrame(self.frame2,width=(self.frame2.winfo_width()/3),height=self.frame2.winfo_height(),text="video")

        self.frame_commentaire.grid_propagate(False)
        self.frame_commentaire.pack_propagate(False)
        self.frame_commentaire.pack(side=LEFT,fill=None, expand=False)

        self.frame_image.grid_propagate(False)
        self.frame_image.pack_propagate(False)
        self.frame_image.pack(side=RIGHT,fill=None, expand=False)

        self.frame_video.grid_propagate(False)
        self.frame_video.pack_propagate(False)
        self.frame_video.pack(side=RIGHT,fill=None, expand=False)

    def affichage_niveaux(self):
        print("appelle de l'affichage")
        self.objet=Simulation.indicateur_niveaux.indicateur_niveaux(self.frame1)

    def plus(self):
        self.objet.value_plus()

    def moins(self):
        self.objet.value_moins()


    def organisation_bouton(self,modif):
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

        self.frame1.grid_propagate(False)   #permet que les frame grade leur taille.
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

        self.logger.info((Nboutton,"ici Nboutton"))
        self.logger.info((PAD,"ici PAD "))
        self.logger.info((DIM,"ici DIM"))
        self.logger.info(int((largeur/Nboutton)//(PAD+DIM)))#calcule nombre de boutton par ligne

        return int(((largeur/Nboutton)//(PAD+DIM)))



    def calcule_points(self):
        document = etree.parse(self.lecture)
        for i in range(len(self.liste_boutton)):#liste_boutton =[[a,b,c],[a,b,c],[a,b,c]]
            for j in range(len(self.liste_boutton[i])):
                parent=self.liste_boutton[i][j]._parent['text']
                nom=self.liste_boutton[i][j]._nom
                value=self.liste_boutton[i][j]._value

                self.logger.info("information parent nom value type(value) pour les erreurs")
                self.logger.info(("parent : ",parent))
                self.logger.info(("nom : ",nom))
                self.logger.info(("valeur : ",value))
                self.logger.info(type(value))
                #print("la valeur atteinte en nombre est ",j)
        self.organisation_erreur()
