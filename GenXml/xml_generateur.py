#!/usr/bin/python3
# -*- coding: utf-8 -*-
import GenXml.Lecture_Settings
import GenXml.Lecture_Donnee
import logging
import verififaction_file_log


dossier="xml_generateur"
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
_logger.info("--------xml_generateur-----------")



def generationXML(fichier):

    def verif(id):
        if id==2 or id==8:
            return "orange"
        else:
            return "green"


    def determine(i,id):
        if ((id>=0 and id<=1) or
        (id>=9 and id <=10)):
            return "eli","red"
        elif id==5:
            return str(0),"green"
        elif parametres._valeurIndiceNegatif == tableau_indice[i]:
            if id>=2 and id<=4:
                value=5-id
                return (str(value),verif(id))
            elif id>=6 and id<=8:
                value=5-id
                return (str(value),verif(id))
        else:
            if id>=2 and id<=4:
                value=id-5
                return (str(value),verif(id))
            elif id>=6 and id<=8:
                value=id-5
                return (str(value),verif(id))

        _logger.debug(tableau_indice[i])



    NomSimple=fichier.split('/')[-1]
    parametres=GenXml.Lecture_Settings.settings()
    if NomSimple.split('.')[1] == 'csv':
        tableau_etape=GenXml.Lecture_Donnee.lecture_fueilles_csv(fichier,parametres._etape)
        tableau_etapePrecision=GenXml.Lecture_Donnee.lecture_fueilles_csv(fichier,parametres._etapePrecision)
        tableau_tabPrincipale=GenXml.Lecture_Donnee.lecture_fueilles_csv(fichier,parametres._tabPrincipale)
        tableau_indice=GenXml.Lecture_Donnee.lecture_fueilles_csv(fichier,parametres._indice)
    else:
        tableau_etape=GenXml.Lecture_Donnee.lecture_fueilles_xlsx(fichier,parametres._etape)
        tableau_etapePrecision=GenXml.Lecture_Donnee.lecture_fueilles_xlsx(fichier,parametres._etapePrecision)
        tableau_tabPrincipale=GenXml.Lecture_Donnee.lecture_fueilles_xlsx(fichier,parametres._tabPrincipale)
        tableau_indice=GenXml.Lecture_Donnee.lecture_fueilles_xlsx(fichier,parametres._indice)

    _logger.debug(tableau_etape)
    _logger.debug(len(tableau_etape))
    _logger.debug("--------------")
    _logger.debug(tableau_etapePrecision)
    _logger.debug(len(tableau_etapePrecision))
    _logger.debug("--------------")
    _logger.debug(tableau_tabPrincipale)
    _logger.debug(len(tableau_tabPrincipale))
    _logger.debug("--------------")
    _logger.debug(tableau_indice)
    _logger.debug(len(tableau_indice))

    file = open("../../fichier_cours/xml/"+NomSimple.split('.')[0]+".xml","w")
    parent=""
    vari=0

     #les liste tableau_etape et tableau_etapePrecision sont similaire dans leur format, la boucle i peux donc géné les 2
    file.write('<?xml version="1.0" encoding="UTF-8"?>'+"\n")
    file.write("<Famille>\n")
    for i in range(len(tableau_etapePrecision)):
        if isinstance(tableau_etape[i][0],str):
            if parent == "":
                parent=tableau_etape[i][0]
                file.write('\t<Pere name="'+tableau_etape[i][0].replace("\n"," ")+'">\n')
                file.write("\t\t"+'<Fils name="'+tableau_etapePrecision[i][0].replace("\n"," ")+'">\n')
            elif tableau_etape[i][0] == parent:
                file.write("\t\t"+'<Fils name="'+tableau_etapePrecision[i][0].replace("\n"," ")+'">\n')
            else:
                parent=tableau_etape[i][0]
                file.write('\t</Pere>\n')
                file.write('\t<Pere name="'+tableau_etape[i][0].replace("\n"," ")+'">\n')
                file.write("\t\t"+'<Fils name="'+tableau_etapePrecision[i][0].replace("\n"," ")+'">\n')

        if isinstance(tableau_etape[i][0],str):
            id=0
            _logger.info(tableau_tabPrincipale[i])
            for j in range(len(tableau_tabPrincipale[i])):
                Titre=[]
                commentaire=[]
                nTitre=0
                nCommentaire=0
                variable=""
                if isinstance(tableau_tabPrincipale[i][j],str):#on ne veux pas les nan qui sont des float (case vide)
                    for k in range(len(str(tableau_tabPrincipale[i][j]))):
                        _logger.info(str(tableau_tabPrincipale[i][j][k]))
                        if variable=="":
                            if tableau_tabPrincipale[i][j][k]=="#":
                                variable="commentaire"
                                commentaire.append("")
                                nCommentaire+=1
                            elif (tableau_tabPrincipale[i][j][k]=='\n' or
                            tableau_tabPrincipale[i][j][k]=='\\' or
                            (tableau_tabPrincipale[i][j][k]=='\\' and tableau_tabPrincipale[i][j][k+1]=='n') or
                            (tableau_tabPrincipale[i][j][k]=='n' and tableau_tabPrincipale[i][j][k-1]=='\\')):
                                variable=""
                            else:
                                variable="titre"
                                Titre.append(tableau_tabPrincipale[i][j][k])
                                _logger.info(Titre)
                                nTitre+=1

                        else:
                            if tableau_tabPrincipale[i][j][k]=="#":
                                variable="commentaire"
                                commentaire.append("")
                                nCommentaire+=1
                            elif tableau_tabPrincipale[i][j][k]=="<":
                                if variable == "commentaire":
                                    commentaire[len(commentaire)-1]+="inférieur"
                                elif variable =="titre":
                                    Titre[len(Titre)-1]+="inférieur"
                            elif tableau_tabPrincipale[i][j][k]==">":
                                if variable == "commentaire":
                                    commentaire[len(commentaire)-1]+="supérieur"
                                elif variable =="titre":
                                    Titre[len(Titre)-1]+="supérieur"
                            elif (tableau_tabPrincipale[i][j][k]=="\n" or
                            tableau_tabPrincipale[i][j][k]=='\\' or
                            (tableau_tabPrincipale[i][j][k]=='\\' and tableau_tabPrincipale[i][j][k+1]=='n') or
                            (tableau_tabPrincipale[i][j][k]=='n' and tableau_tabPrincipale[i][j][k-1]=='\\')):
                                variable=""
                            elif variable=="titre":
                                Titre[len(Titre)-1]+=tableau_tabPrincipale[i][j][k]
                                _logger.info(Titre)
                            elif variable=="commentaire":
                                commentaire[len(commentaire)-1]+=tableau_tabPrincipale[i][j][k]
                                _logger.info(commentaire)
                    variable=""
                    if len(Titre)>0:
                        valeur_petit_fils=""
                        for z in range(len(Titre)):
                            valeur_petit_fils+=('" titre_'+str(z)+'="'+Titre[z])
                        if len(commentaire)>0:
                            for k in range(len(commentaire)):
                                valeur_petit_fils+=('" commentaire_'+str(k)+'="'+commentaire[k])
                            valeur_petit_fils+='"'
                        else:
                            valeur_petit_fils+='"'
                        value,couleur=determine(i,id)
                        file.write('\t\t\t<Petit_Fils id="'+str(id)+valeur_petit_fils+' value="'+value+'" couleur="'+couleur+'"/>\n')
                        id+=1
                    else:
                        valeur_petit_fils=('" titre_0="None"')
                        for z in range(len(commentaire)):
                            valeur_petit_fils+=(' commentaire_'+str(z)+'="'+commentaire[z]+'"')
                        value,couleur=determine(i,id)
                        file.write('\t\t\t<Petit_Fils id="'+str(id)+valeur_petit_fils+' value="'+value+'" couleur="'+couleur+'"/>\n')
                        id+=1

                else:
                    value,couleur=determine(i,id)
                    file.write('\t\t\t<Petit_Fils id="'+str(id)+'" titre_0="None" commentaire_0="None" value="'+value+'" couleur="'+couleur+'"/>\n')
                    id+=1
            file.write('\t\t</Fils>\n')
    file.write('\t</Pere>\n')
    file.write('</Famille>')
    file.close()
