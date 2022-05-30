#!/usr/bin/env python
from tkinter import *
import GenXml.Accueil
import GenXml.Page_chargement
import Simulation.xml_lecture
class MainClass(Tk): #InitFrame érite de toutes les méthodes de la classe tk
    def __init__(self):
        Tk.__init__(self) # nouvelle instante de Tk
        self._MaFrame = None #commance par définir une variable frame qui permet de définir s'il y a une frame ou pas, si oui on la supprime pour en re faire une autre
        #self.switch(Simulation.xml_lecture.Lecture)
        self.switch(GenXml.Page_chargement.Page_chargement)

    def switch(self, frame):
        #destruction de la frame actuelle
        NouvelleFrame = frame(self)
        if self._MaFrame is not None: #=> ducoup si MaFrame n'est pas vide paff on la supprime
            self._MaFrame.destroy()
        self._MaFrame = NouvelleFrame
        try:
            if NouvelleFrame.NomCLASS =="Connexion": #On veux savoir de quelle frame on parle donc ducoup on a une variable de vérification par class
                self._MaFrame.place(relx=0.5, rely=0.5, anchor=CENTER)

            if NouvelleFrame.NomCLASS =="Page_chargement":
                self._MaFrame.place(relx=0.5, rely=0.5, anchor=CENTER)

            if NouvelleFrame.NomCLASS =="Simulation":
                self._MaFrame.place(relx=0.5, rely=0.5, anchor=CENTER)
        except:
            pass


def main():
    windows = MainClass()
    windows.title('Projet')
    windows.geometry("800x600")
    windows.minsize(500,400)
    windows.maxsize(800,600)
    windows.config(background="#FFFFFF")

    windows.mainloop()
