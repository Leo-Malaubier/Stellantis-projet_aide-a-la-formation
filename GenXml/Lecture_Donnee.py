import pandas as pd
import os
import numpy as np


def lecture_fueilles_csv(monfichier,collones_lectures):
    data=[]
    print(monfichier)
    print(type(monfichier))
    print("--------")
    print(collones_lectures)
    print(type(collones_lectures))
    if len(collones_lectures)==1:
        print("Une seul collones")
        liste=[]
        collones_lectures=collones_lectures.lower()
        liste.append(ord(collones_lectures)-97) #on transforme la lettre en chiffre pour la lecture du tableau (-96 car code askii donc a=1 et -97 a=0)
        temps=pd.read_csv(monfichier, usecols=liste)
        print(temps)
    else:
        print("plusieur colones")
        liste=[]
        collones_lectures=collones_lectures.lower()
        print(collones_lectures)
        for i in range(ord(collones_lectures[0])-97, ord(collones_lectures[2])-96):
            liste.append(i)
            temps=pd.read_csv(monfichier, usecols=liste)
        print(temps)
    Np=temps.to_numpy()
    return Np

#spécificité de read_csv: ne prend que des numéreau de collones_lectures
#tandis que la lecture xlsx est plus libre dans le forma de lecture

def lecture_fueilles_xlsx(monfichier,collones_lectures):
    data=[]
    temps=pd.read_excel(monfichier, usecols=collones_lectures)
    Np=temps.to_numpy()
    return Np
