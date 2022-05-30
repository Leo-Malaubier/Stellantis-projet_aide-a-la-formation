from tkinter import *
from lxml import etree
import Simulation.boutton_valeur
import Simulation.Erreur
class Lecture(Frame):
    NomCLASS ="Simulation"
    def __init__(self,pere):
        Frame.__init__(self, pere)
        self._pere=pere

        self.boutton=Simulation.boutton_valeur.Valeur(self._pere)
        self.boutton.pack()

        file=open("temp/temporaire.txt","r")
        ligne=file.readlines(0)
        #lien complet du fichier(/!\ il peux y avoir un \n)
        try:
            self.lecture=ligne[0].split('\n')[0]
        except:
            self.lecture=ligne[0]
        if self.lecture.split(".")[1]== "xlsx" or self.lecture.split(".")[1]=="csv":
            self.lecture="xml/"+ligne[1].split(".")[0]+".xml"
        else:
            self.lecture="xml/"+ligne[1]
        Button(self, text="actualise",command = self.refresh).pack()
        self.affichage()
        self.organisation()

    def refresh(self):
        self.frame3.delete(ALL)
        self.organisation()

    def affichage(self):
        self.frame1=Frame(self._pere,bg="brown")
        self.frame2=Frame(self._pere,bg="green")
        self.frame3=Frame(self._pere,bg="#FFFFFF")

        self.liste_label_frame_pere=[]
        self.liste_boutton=[]
        document = etree.parse(self.lecture)
        for pere in document.xpath("/Famille/Pere"):
            #print(pere.get("name"))
            #print(len(pere))

            self.liste_label_frame_pere.append(LabelFrame(self.frame3,relief=RAISED,text=pere.get("name")))
            liste_temp_boutton=[]
            for i in range(len(pere)):
                fils=pere[i].get("name")
                liste_temp_boutton.append(Simulation.boutton_valeur.Valeur(self.liste_label_frame_pere[len(self.liste_label_frame_pere)-1]))
                #print(fils)#nom fils

            self.liste_boutton.append(liste_temp_boutton)


    def organisation(self):
        max=self.max_boutton_ligne()
        for i in range(len(self.liste_boutton)):
            collone=0
            ligne=0
            print(self.liste_boutton)
            print(len(self.liste_boutton))
            for j in range(len(self.liste_boutton[i])):
                if j%max==0:
                    collone=0
                    ligne+=1
                else:
                    collone+=1

                self.liste_boutton[i][j]._l=ligne
                self.liste_boutton[i][j]._c=collone
                self.liste_boutton[i][j].creation(str(i))
        self.grid_pack()

    def grid_pack(self):
        for i in range(len(self.liste_label_frame_pere)):
            self.liste_label_frame_pere[i].grid(column=i,row=0)
            print(self.liste_label_frame_pere[i], "est paqué")
        self.frame3.pack(side="bottom")

    def max_boutton_ligne(self):
        largeur=self._pere.winfo_width()
        print(largeur)
        PAD=self.liste_boutton[0][0].PAD
        DIM=self.liste_boutton[0][0].DIM
        Nboutton=len(self.liste_boutton)
        print(int((largeur/Nboutton)//(PAD+DIM)))#calcule nombre de boutton par ligne

        return int(((largeur/Nboutton)//(PAD+DIM)))

"""
for j in range(len(pere[i])):
    print(pere[i][j].get("id"))#id petit_fils /!\ l'id est de type str
    print(type(pere[i][j].get("id")))
    liste_label_frame_fils.append(Simulation.boutton_valeur.Valeur())
"""
