#!/usr/bin/env python

# -*- coding: utf-8 -*-

import pandas as pd
import os
import numpy as np

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

_logger = logging.getLogger()

def lecture_fueilles_csv(monfichier,collones_lectures):
    _logger.info("--------Lecture_Donnee-----------")
    data=[]
    # _logger.debug(monfichier)
    # _logger.debug(type(monfichier))
    # _logger.debug("--------")
    # _logger.debug(collones_lectures)
    # _logger.debug(type(collones_lectures))
    if len(collones_lectures)==1:
        _logger.info("Une seul collones")
        liste=[]
        collones_lectures=collones_lectures.lower()
        liste.append(ord(collones_lectures)-97) #on transforme la lettre en chiffre pour la lecture du tableau (-96 car code askii donc a=1 et -97 a=0)
        temps=pd.read_csv(monfichier, usecols=liste)
        _logger.info(temps)
    else:
        _logger.info("plusieur colones")
        liste=[]
        collones_lectures=collones_lectures.lower()
        _logger.info(collones_lectures)
        for i in range(ord(collones_lectures[0])-97, ord(collones_lectures[2])-96):
            liste.append(i)
            temps=pd.read_csv(monfichier, usecols=liste)
        _logger.info(temps)
    Np=temps.to_numpy()
    return Np


#spécificité de read_csv: ne prend que des numéreau de collones_lectures
#tandis que la lecture xlsx est plus libre dans le forma de lecture


def lecture_fueilles_xlsx(monfichier,collones_lectures):
    data=[]
    temps=pd.read_excel(monfichier, usecols=collones_lectures)#engine='openpyxl'
    Np=temps.to_numpy()
    return Np
