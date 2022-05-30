#!/usr/bin/env python

# -*- coding: utf-8 -*-

from tkinter import *
import math
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



class Valeur(Frame):
    logger = logging.getLogger()
    PAD=25 #marge pour que le cercle ne soit pas collé au bord du canvas
    DIM=80 #diamètre


    def __init__(self,pere):
        self.logger.info("--------boutton_valeur-----------")

        self._value=0
        self._nom=""
        self._id=0

        self._parent=pere #frame parente
        self._c=0 #collone
        self._l=0#ligne


        Frame.__init__(self,master=self._parent)

        self.couleur_boutton="#DF9595"
        self.couleur_background="#FFFFFF"
        self.WIDTH=self.DIM+self.PAD
        self.HEIGHT=self.DIM+self.PAD

        self.centre = (self.WIDTH//2, self.HEIGHT//2)#centre cercle

        self.nombre_valeur=11 #on a des valeur allant de 0 à 10
        self.angle_init=180 #angle plat pour que l'on affiche nos valeur dans la partie supérieur du create_rectangle

        self.posi=0
        self.coef=1.1


    def affichage(self):

        #Frame.__init__(self,master=self._parent)
        self["width"]=100
        self["height"]=50
        self["bd"]=1
        self["relief"]=RAISED

        button=self.button()
        self.cnv.pack()
        self.position()
        self.posi=(0,self.WIDTH/self.coef)
        self.cnv.create_text(self.posi, anchor =W,text =self._nom,fill ="black") #affichage nom boutton


    def position(self):
        self.grid(column=self._c,row=self._l)

    def ligne_modif(self):
        i=self._value
        R=self.DIM//2
        xC, yC=self.centre
        if i!=0:
            angle_inter_element=self.angle_init-self.angle_init/self.nombre_valeur*-i
            xMax=xC+R//1*math.cos(math.radians(angle_inter_element))#on prend le quotient du rayon //9 pour faire calculer une ligne
            yMax=yC+R//1*math.sin(math.radians(angle_inter_element))
            xMin=xC+R//4*math.cos(math.radians(angle_inter_element))#on prend le quotient du rayon //9 pour faire calculer une ligne
            yMin=yC+R//4*math.sin(math.radians(angle_inter_element))
            self.cnv.coords(self.ligne,xMax,yMax,xMin,yMin)
        else:#on évite la division et multiplication par 0
            xMax=xC+R//1*math.cos(math.radians(i+180))
            yMax=yC+R//1*math.sin(math.radians(i))
            xMin=xC+R//4*math.cos(math.radians(i+180))
            yMin=yC+R//4*math.sin(math.radians(i))
            self.cnv.coords(self.ligne,xMax,yMax,xMin,yMin)

    def value_plus(self,position=None):#position est l'endroit ou le clique a lieu. il n'est pas utile mais est retourné par le clique souris
        if self._value == 10:
            self._value=self._value
        else:
            self._value+=1
        self.cnv.itemconfig(self.text,text=str(self._value))
        self.ligne_modif()

    def value_moins(self,position=None):
        if self._value == 0:
            self._value=self._value
        else:
            self._value-=1
        self.logger.debug("clique moins")
        self.cnv.itemconfig(self.text,text=str(self._value))
        self.ligne_modif()

    def creation(self,information):
        self._id=information
        #self._id=id
        self.affichage()

    def set_nom(self,information):
        if " " in information:
            information=information.replace(" ","\n")
            self.coef=1.2
        self._nom=information

    def change_couleur(self,couleur):
        self.label_frame['bg']=couleur


    def button(self):
        self.cnv = Canvas(self, width=self.WIDTH, height=self.HEIGHT, background=self.couleur_background)
        def dot( R, color=self.couleur_boutton):#canva, centre, rayon, couleur
            xC, yC=self.centre
            A=(xC-R, yC-R)#on calcule les point supérieur gauche et inférieur droit du carré dans le quelle le cercle rentre. (voir comment sont créer les cercle dans tkinter)
            B=(xC+R, yC+R)
            return self.cnv.create_oval(A,B, fill=color, outline=color)

        R=self.DIM//2
        dot(R) #R= rayon

        xC, yC=self.centre #x,y du centre
        for i in range(self.nombre_valeur): #i correspond au nombre de crant du boutton (plus ou moins)
            if i!=0:
                angle_inter_element=self.angle_init-self.angle_init/self.nombre_valeur*-i
                #angle_inter_element = self.angle_init - self.angle_init/self.nombre_valeur*i
                x=xC+R*math.cos(math.radians(angle_inter_element))
                y=yC+R*math.sin(math.radians(angle_inter_element))
                if i<6: #petit ajustement pour que les nombre soit affiché en dehor du cercle
                    x-=10
                    y-=3
                if i>=6:
                    y-=4
                position=(x,y)
                self.logger.info("i dif 0/ voici x:"+str(x)+" et voici y:"+str(y)+" i="+str(i))
                self.cnv.create_text(position, anchor =W,text =i,fill ="black")
            else:#on évite la division et multiplication par 0
                x=xC+R*math.cos(math.radians(i+180))
                y=yC+R*math.sin(math.radians(i))
                position=(x-10,y)
                self.logger.info("i == 0/ voici x:"+str(x)+" et voici y:"+str(y)+" i="+str(i))
                self.cnv.create_text(position, anchor =W,text =i,fill ="black")
        self.text=self.cnv.create_text(self.centre,text="0")
        angle_inter_element=self.angle_init-self.angle_init/self.nombre_valeur*-0
        xMax=xC+R//1*math.cos(math.radians(i+180))
        yMax=yC+R//1*math.sin(math.radians(i))
        xMin=xC+R//4*math.cos(math.radians(i+180))
        yMin=yC+R//4*math.sin(math.radians(i))
        self.ligne=self.cnv.create_line(xMax,yMax,xMin,yMin, width=4, fill="#000000")


        self.cnv.bind("<Button-1>", self.value_plus)
        self.cnv.bind("<Button-3>", self.value_moins)
