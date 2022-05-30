#!/usr/bin/env python
from tkinter import *
from tkinter import filedialog
from tkinter import messagebox #permet de faire des message d'alert
#installer le module pandas et openpyxl
import pandas as pd #lire les fichier excel
import shutil #permet de copier un fichier
import os #permet de géré des fichier
import logging

import GenXml.converXlsx_to_csv
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


class Recherche:

    _logger = logging.getLogger()

    def __init__(self,xml):
        self._logger.info("la recherche ce lance")
        self.emplacement_fichier="../../fichier_cours/"
        emplacement_fichier_xml="../../fichier_cours/xml/"
        filename=None
        if xml == None:
            filename = filedialog.askopenfilename(initialdir = self.emplacement_fichier,title = "Select a File",filetypes = (("Text files","*.xlsx*"),("Text files","*.csv*"),("all files","*.*")))
        elif xml == "xml":
            filename = filedialog.askopenfilename(initialdir = emplacement_fichier_xml,title = "Select a File",filetypes = (("Text files","*.xml*"),("all files","*.*")))

        self.f= filename  #nom du fichier
        self.ConvertXlsxToCsv()


    def ConvertXlsxToCsv(self): #permet d'ouvrir le fichier d'on on a le lien en fait une copie et transforme cette copie en csv
        source=self.f
        self.NomSimple=source.split('/')[-1]
        if self.NomSimple.split('.')[1]=="xlsx":
            demande=messagebox.askquestion(title="Conversion xlsx to csv", message="Voulez vous convertir votre fichier "+self.NomSimple+"en fichier csv?")
            if demande == "yes" :
                GenXml.converXlsx_to_csv.csv_to_excel(self.f)
                self.f=self.emplacement_fichier+"csv/"+self.NomSimple.split(".")[0]+".csv"
            if demande == "no" :
                pass
