#!/usr/bin/env python

# -*- coding: utf-8 -*-

from tkinter import *
import GenXml.Page_chargement
import main
#import Selection

class Connexion(Frame):
    NomCLASS ="Connexion"
    def __init__(self, pere):
        Frame.__init__(self, pere)
        #self.config(bg ='black',bd=1, padx=50, pady=20)
        self._pere=pere

        resultButton = Button(self, text = 'Démarrer la simulation',command=self.Login)
        resultButton.grid()
        resultButton = Button(self, text = 'QCM',command=self.Login)
        resultButton.grid()
        #supButton = Button(self.fra, text = 'sup',command=self.dest)
        #supButton.grid(column=1, row=2, pady=10)



    def Login(self): #connexion avec affichage des erreur
        self._pere.switch(GenXml.Page_chargement.Page_chargement)
