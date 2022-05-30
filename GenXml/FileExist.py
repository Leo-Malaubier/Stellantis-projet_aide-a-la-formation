#!/usr/bin/env python

# -*- coding: utf-8 -*-

import os
def verification():
    if not os.path.exists('../../fichier_cours'):
        os.makedirs('../../fichier_cours')
    if not os.path.exists('../../fichier_cours/xml'):
        os.makedirs('../../fichier_cours/xml')
    if not os.path.exists('../../fichier_cours/xlsx'):
        os.makedirs('../../fichier_cours/xlsx')
    if not os.path.exists('../../fichier_cours/csv'):
        os.makedirs('../../fichier_cours/csv')
    if not os.path.exists('../../fichier_cours/parametres'):
        os.makedirs('../../fichier_cours/parametres')
    return 'Done'
