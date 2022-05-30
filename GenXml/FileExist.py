#!/usr/bin/env python

# -*- coding: utf-8 -*-

import os
emplacement_fichier="../../fichier_cours/"


def verification():
    if not os.path.exists(emplacement_fichier):
        os.makedirs(emplacement_fichier)
    if not os.path.exists(emplacement_fichier+'xml'):
        os.makedirs(emplacement_fichier+'xml')
    if not os.path.exists(emplacement_fichier+'xlsx'):
        os.makedirs(emplacement_fichier+'xlsx')
    if not os.path.exists(emplacement_fichier+'csv'):
        os.makedirs(emplacement_fichier+'csv')
    if not os.path.exists(emplacement_fichier+'parametres'):
        os.makedirs(emplacement_fichier+'parametres')
    return 'Done'
