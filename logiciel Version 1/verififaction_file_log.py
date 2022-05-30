import os
import logging
def verification_file(dossier="log",emplacement_log="log/",emplacement_log_init="log/"):
    file_size = os.stat(emplacement_log+dossier+'.log')
    if file_size.st_size >= 1000000: #quand le fichier des log atteint la taille de 1Mo on le suprrime et on en créer un nouveau pour pas prend trop de place
        myFile = open(emplacement_log+dossier+'.log', "w")
        myFile.close()
    if not os.path.exists(emplacement_log_init):
        os.makedirs(emplacement_log_init)
    if not os.path.exists(emplacement_log):
        os.makedirs(emplacement_log)
    try:
        with open(emplacement_log+dossier+'.log'):pass
    except:
        myFile = open(emplacement_log+dossier+'.log', "w")
        myFile.close()
    logging.basicConfig(filename=emplacement_log+dossier+'.log', level=logging.DEBUG,
                            format='%(asctime)s - %(levelname)s:%(message)s')
    logging.info('----- Taille_fichier_log -----')
    logging.info(('File Size is', file_size.st_size, 'bytes'))
