#!/usr/bin/env python
from tkinter import *
from tkinter import filedialog
from tkinter import messagebox #permet de faire des message d'alert
#installer le module pandas et openpyxl
import pandas as pd #lire les fichier excel
import shutil #permet de copier un fichier
import os #permet de géré des fichier
import GenXml.converXlsx_to_csv

class Recherche:
    def __init__(self,xml):
        #print("la recherche ce lance")
        filename=None
        if xml == None:
            filename = filedialog.askopenfilename(initialdir = "../../fichier_cours/",title = "Select a File",filetypes = (("Text files","*.xlsx*"),("Text files","*.csv*"),("all files","*.*")))
        elif xml == "xml":
            filename = filedialog.askopenfilename(initialdir = "../../fichier_cours/xml/",title = "Select a File",filetypes = (("Text files","*.xml*"),("all files","*.*")))

        self.f= filename  #nom du fichier
        self.ConvertXlsxToCsv()


    def ConvertXlsxToCsv(self): #permet d'ouvrir le fichier d'on on a le lien en fait une copie et transforme cette copie en csv
        source=self.f
        self.NomSimple=source.split('/')[-1]
        if self.NomSimple.split('.')[1]=="xlsx":
            demande=messagebox.askquestion(title="Conversion xlsx to csv", message="Voulez vous convertir votre fichier "+self.NomSimple+"en fichier csv?")
            if demande == "yes" :
                GenXml.converXlsx_to_csv.csv_to_excel(self.f)
                self.f="../../fichier_cours/csv/"+self.NomSimple.split(".")[0]+".csv"
            if demande == "no" :
                pass
