#!/usr/bin/env python
from tkinter import *
from tkinter import messagebox #permet de faire des message d'alert

import GenXml.recherche
import GenXml.xml_generateur
import Simulation.xml_lecture
class Page_chargement(Frame):
    NomCLASS= "Page_chargement"
    def __init__(self, pere):
        Frame.__init__(self, pere)
        self._pere=pere
        self._token_fichier=None

        Button(self, text ="Ajouté une fichier (csv/xlsx)", command = self.execution).pack()
        Button(self,text="Ajouté un fichier xml",command=self.rechercheXml).pack()
        Button(self, text="Démarrer la simulation",command = self.start).pack()

    def execution(self):
        self._token_fichier=GenXml.recherche.Recherche(None)
        #génération xml
        print(self._token_fichier.f)
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
