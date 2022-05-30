#!/usr/bin/env python

# -*- coding: utf-8 -*-

import pandas as pd
import os
def csv_to_excel(file):
    nomSimple=file.split("/")[-1]
    read_file = pd.read_excel(file)
    read_file.to_csv ("../../fichier_cours/csv/"+nomSimple.split('.')[0]+".csv",
                      index = None,
                      header=True)
    df = pd.DataFrame(pd.read_csv("../../fichier_cours/csv/"+nomSimple.split('.')[0]+".csv"))
