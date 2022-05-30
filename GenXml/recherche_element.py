#!/usr/bin/env python

# -*- coding: utf-8 -*-

import GenXml.FileExist
import os
import logging
import verififaction_file_log


emplacement_fichier="../../fichier_cours/"
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
_logger.info("--------recherche-----------")
def traitement(list,type_fichier):
    MALISTE=[]
    for i in range(len(list)):
        try:
            if list[i].split('.')[1]==type_fichier:
                MALISTE.append(list[i])
        except:
            pass
    return MALISTE


def rangement():

    liste=(os.listdir("../../fichier_cours"))
    Liste=[]
    _logger.debug(liste)

    for i in range(len(liste)):
        try:
            _logger.debug(type(liste[i].split('.')[1]))
            if isinstance(liste[i].split('.')[1],str)== True:
                Liste.append(liste[i])
        except:
            pass
    _logger.debug(Liste)
    for i in range(len(Liste)):
        src=emplacement_fichier+Liste[i]
        if Liste[i].split('.')[1]=='xlsx':
            des=emplacement_fichier+'xlsx/'+Liste[i]
            os.replace(src,des)
        if Liste[i].split('.')[1]=='csv':
            des=emplacement_fichier+'csv/'+Liste[i]
            os.replace(src,des)
        if Liste[i].split('.')[1]=='xml':
            des=emplacement_fichier+'xml/'+Liste[i]
            os.replace(src,des)


def ListeFichier(emplacement,type_fichier): #liste de nom des fichiers
        if type_fichier=='rangement':
            return rangement()
        else:
            list =(os.listdir(emplacement))
        if type_fichier=="xlsx" or type_fichier=="csv" or type_fichier=="xml":
            return traitement(list,type_fichier)



def recherche_element():
    GenXml.FileExist.verification()
    ListeFichier('rangement','rangement')
    xlsx=ListeFichier(emplacement_fichier+"xlsx","xlsx")
    csv=ListeFichier(emplacement_fichier+"csv","csv")
    xml=ListeFichier(emplacement_fichier+"xml","xml")
    return xlsx,csv,xml
