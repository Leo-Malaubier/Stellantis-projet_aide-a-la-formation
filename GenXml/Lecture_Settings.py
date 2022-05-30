#!/usr/bin/env python

# -*- coding: utf-8 -*-
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

class settings:
    _logger = logging.getLogger()
    _collones =""
    _etape =""
    _etapePrecision =""
    _tabPrincipale =""
    _indice =""
    _valeurIndiceNegatif =""
    _valeurIndicePositif =""
    _titreCase =""
    _commentaireCase =""
    _separateurRetourLigne =""


    def __init__(self):
        self._logger.info("--------Lecture_Settings-----------")
        file=open("parametres/setting.txt","r")
        text=file.readlines() #attention à la différence entre readline et readlines
        self._logger.info(len(text))
        for i in range(len(text)):
            if text[i][0]!="#" and text[i][0]+text[i][1]!="\n": #éviton les commentaires et les retour a la ligne
                self.numbers_to_strings(text[i])
        file.close()


    def numbers_to_strings(self,argument):
        argument=argument.replace(" ","")
        valeur=argument.split('{')
        valeur1=valeur[0]
        valeur2=valeur[1].split('}')[0]#comme sa on évite le \n de fin de ligne
        self._logger.info((valeur1,"/",valeur2))
        #j'aurais voulus utilisé un switch, mais le switch parcour toutes les option et exectute tou les self donc la meilleur option est une suite de if
        if valeur1 =="collones" :
            self.setcollones(valeur2)
        if valeur1 == "etape" :
            self.setetape(valeur2)
        if valeur1 == "etapePrecision" :
            self.setetapePrecision(valeur2)
        if valeur1 == "tabPrincipale" :
            self.settabPrincipale(valeur2)
        if valeur1 == "indice" :
            self.setindice(valeur2)
        if valeur1 == "valeurIndiceNegatif" :
            self.setvaleurIndiceNegatif(valeur2)
        if valeur1 == "valeurIndicePositif" :
            self.setvaleurIndicePositif(valeur2)
        if valeur1 == "titreCase" :
            self.settitreCase(valeur2)
        if valeur1 == "commentaireCase" :
            self.setcommentaireCase(valeur2)
        if valeur1 == "separateurRetourLigne" :
            self.setseparateurRetourLigne(valeur2)

    def setcollones(self,valeur):
        self._collones=valeur
        self._logger.info(self._collones)

    def setetape(self,valeur):
        self._etape=valeur
        self._logger.info(self._etape)

    def setetapePrecision(self,valeur):
        self._etapePrecision=valeur
        self._logger.info(self._etapePrecision)

    def settabPrincipale(self,valeur):
        self._tabPrincipale=valeur
        self._logger.info(self._tabPrincipale)

    def setindice(self,valeur):
        self._indice=valeur
        self._logger.info(self._indice)

    def setvaleurIndiceNegatif(self,valeur):
        self._valeurIndiceNegatif=valeur
        self._logger.info(self._valeurIndiceNegatif)

    def setvaleurIndicePositif(self,valeur):
        self._valeurIndicePositif=valeur
        self._logger.info(self._valeurIndicePositif)

    def settitreCase(self,valeur):
        self._titreCase=valeur
        self._logger.info(self._titreCase)

    def setcommentaireCase(self,valeur):
        self._commentaireCase=valeur
        self._logger.info(self._commentaireCase)

    def setseparateurRetourLigne(self,valeur):
        self._separateurRetourLigne=valeur
        self._logger.info(self._separateurRetourLigne)
