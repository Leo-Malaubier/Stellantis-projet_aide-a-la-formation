
class settings:

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
        file=open("parametres/setting.txt","r")
        text=file.readlines() #attention à la différence entre readline et readlines
        print(len(text))
        for i in range(len(text)):
            if text[i][0]!="#" and text[i][0]+text[i][1]!="\n": #éviton les commentaires et les retour a la ligne
                self.numbers_to_strings(text[i])
        file.close()


    def numbers_to_strings(self,argument):
        argument=argument.replace(" ","")
        valeur=argument.split('{')
        valeur1=valeur[0]
        valeur2=valeur[1].split('}')[0]#comme sa on évite le \n de fin de ligne
        print(valeur1,"/",valeur2)
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
    def setetape(self,valeur):
        self._etape=valeur
    def setetapePrecision(self,valeur):
        self._etapePrecision=valeur
    def settabPrincipale(self,valeur):
        self._tabPrincipale=valeur
    def setindice(self,valeur):
        self._indice=valeur
    def setvaleurIndiceNegatif(self,valeur):
        self._valeurIndiceNegatif=valeur
    def setvaleurIndicePositif(self,valeur):
        self._valeurIndicePositif=valeur
    def settitreCase(self,valeur):
        self._titreCase=valeur
    def setcommentaireCase(self,valeur):
        self._commentaireCase=valeur
    def setseparateurRetourLigne(self,valeur):
        self._separateurRetourLigne=valeur

"""
variable=settings()
print(variable._collones)
print(variable._etape)
print(variable._etapePrecision)
print(variable._tabPrincipale)
print(variable._indice)
print(variable._valeurIndiceNegatif)
print(variable._valeurIndicePositif)
print(variable._titreCase)
print(variable._commentaireCase)
print(variable._separateurRetourLigne)
"""
