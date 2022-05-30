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

class ajout_cours(Frame):

    NomCLASS= "Ajour_cours"
    _logger = logging.getLogger()

    def __init__(self, pere):
        self._logger.info("--------ajout_cours-----------")
        Frame.__init__(self, pere)

        self._pere=pere
        self._token_fichier=None

        Button(self, text ="Ajouté une fichier (csv/xlsx)", command = self.execution).pack()
        Button(self,text="Ajouté un fichier xml",command=self.rechercheXml).pack()
        Button(self, text="Démarrer la simulation",command = self.start).pack()
        Button(self, text="retour",command = self.retour).pack()

        self.pack()


    def execution(self):
        self._token_fichier=GenXml.recherche.Recherche(None)
        #génération xml
        self._logger.info(self._token_fichier.f)
        GenXml.xml_generateur.generationXML(self._token_fichier.f)


    def rechercheXml(self):
        self._token_fichier=GenXml.recherche.Recherche("xml")


    def start(self):
        if self._token_fichier == None:
            messagebox.showwarning(title="Attention erreur de remplissage", message="Vous devez sélectioné un fichier à chargé")
        else:
            file=open("temp/temporaire.txt","w")
            file.write(self._token_fichier.f)
            file.write('\n')
            file.write(self._token_fichier.NomSimple)
            file.close()
            self._pere.switch(Simulation.xml_lecture.Lecture)

            
    def retour(self):
        self._pere.switch(GenXml.Page_chargement.Page_chargement)
