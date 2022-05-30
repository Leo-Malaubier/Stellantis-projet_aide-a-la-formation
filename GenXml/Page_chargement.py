#!/usr/bin/env python

# -*- coding: utf-8 -*-

from tkinter import *
from tkinter import messagebox #permet de faire des message d'alert
from tkinter import ttk

import GenXml.recherche
import GenXml.xml_generateur
import Simulation.xml_lecture
import GenXml.recherche_element

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

class Page_chargement(Frame):
    
    _logger = logging.getLogger()
    NomCLASS= "Page_chargement"

    def __init__(self, pere):
        self._logger.info("--------Page_chargement-----------")
        Frame.__init__(self, pere)

        self._pere=pere

        Button(self,text="Charger un nouvel exercice",command=self.charger_nouveaux_cour).pack(side=BOTTOM)
        Button(self, text="Démarrer la simulation",command = self.start).pack(side=BOTTOM)

        self.label_frame=LabelFrame(self,relief=RAISED,text='Cours')

        self.treeview=ttk.Treeview(self.label_frame,columns=1,show='',height=3)
        self.treeview.heading(1,text='Cours')

        scrollbar = Scrollbar(self.label_frame,orient=VERTICAL,command=self.treeview.yview)
        self.treeview.configure(yscroll=scrollbar.set)
        scrollbar.pack(side=RIGHT,fill=Y)
        self.treeview.pack(side=LEFT)

        self.label_frame.pack()

        self.liste=[]#liste comptenue du treeview
        self.treeviewActualise()

        self.emplacement_fichier="../../fichier_cours/"


    def treeviewActualise(self):
        xlsx,csv,xml=GenXml.recherche_element.recherche_element()
        self._logger.info(str(xlsx))
        self._logger.info(str(csv))
        self._logger.info(str(xml))
        for i in xml:
            self.liste.append(i)
        for i in  range(len(csv)):
            self.activ(csv[i])
        for i in  range(len(xlsx)):
            self.activ(xlsx[i])
        self._logger.info((self.liste,"voici la liste sans traitement"))
        if len(self.liste)==0:
            self.affiche_erreur("liste_vide")
        for i in range(len(self.liste)):
            self.treeview.insert(parent='', index=i,iid=i,values=(self.liste[i].split('.')[0]))


    def activ(self,a): #fonction déclanchement de la récursivité
        self.verif(a,self.liste,0)



    def verif(self,a,b,val):
        if len(b)==0:
            self.liste.append(a)
            return 'append'
        if len(b)-1 == val:
            if a.split('.')[0] != b[val].split('.')[0]:
                self._logger.info("apprendre")
                self.liste.append(a)
                return 'append'
            else:
                return 'no'
        if a.split('.')[0]!= b[val].split('.')[0]:
            self.verif(a,b,val+1)
        if a.split('.')[0]==b[val].split('.')[0]:
            return 'no'


    def execution(self,fichier_select):
        fichier_select=self.liste[int(fichier_select[0])]
        self._logger.debug(fichier_select)
        if fichier_select.split(".")[1]=="csv":
            fichier_select=self.emplacement_fichier+"csv/"+fichier_select
            GenXml.xml_generateur.generationXML(fichier_select)
        if fichier_select.split(".")[1]=="xlsx":
            fichier_select=self.emplacement_fichier+"xlsx/"+fichier_select
            GenXml.xml_generateur.generationXML(fichier_select)
        if fichier_select.split(".")[1]=="xml":
            fichier_select=self.emplacement_fichier+"xml/"+fichier_select
        #génération xml
        self._logger.debug(fichier_select,)
        return fichier_select


    def charger_nouveaux_cour(self):
        self._pere.switch(GenXml.ajout_cours.ajout_cours)


    def start(self):
        selection=self.treeview.selection()
        if len(selection)>1:
            self.affiche_erreur("liste_select_plaine")
        if len(selection)==0:
            self.affiche_erreur("liste_select_vide")
        if len(selection)==1:
            lien_fichier=self.execution(selection)
            file=open("temp/temporaire.txt","w")
            file.write(lien_fichier)
            file.write('\n')
            file.write(lien_fichier.split('/')[-1])
            file.close()
            self._pere.switch(Simulation.xml_lecture.Lecture)



    def affiche_erreur(self,type):
        try:
            self.labelErr.destroy()
        except:
            pass
        if type == "liste_vide":
            self.labelErr=Label(self.label_frame,text="Il n'y a aucun cour dans les fichiers,\n veuillez chargé de nouveaux cours")
            self.labelErr.pack(side=BOTTOM)
            messagebox.showinfo(title="Attention erreur de remplissage", message="Il n'y a aucun cour dans les fichiers,\n veuillez chargé de nouveaux cours")
        if type =="liste_select_plaine":
            self.labelErr=Label(self.label_frame,text="vous ne devez sélectioné qu'un seul cour")
            self.labelErr.pack(side=BOTTOM)
            messagebox.showinfo(title="Attention erreur de remplissage", message="Vous avez sélectionné trop de cours. \n vous ne devez sélectionné qu'un seul cours")
        if type == "liste_select_vide":
            self.labelErr=Label(self.label_frame,text="vous ne devez sélectioné un cour")
            self.labelErr.pack(side=BOTTOM)
            messagebox.showinfo(title="Attention erreur de remplissage", message="Vous avez devez sélectioné un cour")
