#!/usr/bin/env python

# -*- coding: utf-8 -*-

import GenXml.FileExist
import os
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
    print(liste)

    for i in range(len(liste)):
        try:
            print(type(liste[i].split('.')[1]))
            if isinstance(liste[i].split('.')[1],str)== True:
                Liste.append(liste[i])
        except:
            pass
    print(Liste)
    for i in range(len(Liste)):
        src=r'../../fichier_cours/'+Liste[i]
        if Liste[i].split('.')[1]=='xlsx':
            des=r'../../fichier_cours/xlsx/'+Liste[i]
            os.replace(src,des)
        if Liste[i].split('.')[1]=='csv':
            des=r'../../fichier_cours/csv/'+Liste[i]
            os.replace(src,des)
        if Liste[i].split('.')[1]=='xml':
            des=r'../../fichier_cours/xml/'+Liste[i]
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
    xlsx=ListeFichier("../../fichier_cours/xlsx","xlsx")
    csv=ListeFichier("../../fichier_cours/csv","csv")
    xml=ListeFichier("../../fichier_cours/xml","xml")
    return xlsx,csv,xml
