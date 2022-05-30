#!/usr/bin/env python

# -*- coding: utf-8 -*-

from tkinter import *
import GenXml.Accueil
import GenXml.Page_chargement
import GenXml.ajout_cours
import Simulation.xml_lecture
import verififaction_file_log
class MainClass(Tk): #InitFrame érite de toutes les méthodes de la classe tk
    def __init__(self):
        Tk.__init__(self) # nouvelle instante de Tk
        self._MaFrame = None #commance par définir une variable frame qui permet de définir s'il y a une frame ou pas, si oui on la supprime pour en re faire une autre
        #self.switch(Simulation.xml_lecture.Lecture)
        self.switch(GenXml.Accueil.Connexion) #premier page a charger

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
            if NouvelleFrame.NomCLASS =="Ajour_cours":
                self._MaFrame.place(relx=0.5, rely=0.5, anchor=CENTER)
        except:
            pass


def main():
    verififaction_file_log.verification_file()
    windows = MainClass()
    windows.title('Projet')

    w, h = windows.winfo_screenwidth(), windows.winfo_screenheight()
    #windows.geometry("%dx%d" % (w, h))
    windows.geometry("1000x800")
    windows.update_idletasks()
    windows.resizable(width=False, height=False)
    windows.config(background="#FFFFFF")

    windows.mainloop()
if __name__ == "__main__":
    main()
