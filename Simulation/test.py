from tkinter import *
import Erreur
import boutton_valeur
windows = Tk()
windows.title('Projet')
windows.geometry("800x600")
windows.minsize(500,400)
windows.maxsize(800,600)
windows.config(background="#FFFFFF")

frame1=Frame(windows,bg="brown")
frame2=Frame(windows,bg="green")
frame3=Frame(windows,bg="#FFFFFF")

label_frame =LabelFrame(frame3,width=100,height=50,bd=1,relief=RAISED,text="test",bg="#FFFFFF")
label_frame2 =LabelFrame(frame3,width=100,height=50,bd=1,relief=RAISED,text="testrfd",bg="#FFFFFF")



err=Erreur.Erreur(frame1)
err.creation(["red",["erreur","erreur seconde"],["commentaire1","commentaire2"],"parent"])

listeButton=[]
listeButton2=[]
for i in range(5):
    boutton=boutton_valeur.Valeur(label_frame)
    listeButton.append(boutton)
    boutton2=boutton_valeur.Valeur(label_frame2)
    listeButton2.append(boutton2)

collone=0
ligne=0
for i in range(len(listeButton)):
    if i%3==0:
        collone=0
        ligne+=1
    else:
        collone+=1

    listeButton[i]._l=ligne
    listeButton[i]._c=collone
    listeButton2[i]._l=ligne
    listeButton2[i]._c=collone
    listeButton[i].creation(str(i))
    listeButton2[i].creation(str(i))



label_frame.grid(column=0,row=0)
label_frame2.grid(column=1,row=0)

frame1.pack(side="top")
frame2.pack()
frame3.pack(side="bottom")
windows.mainloop()
