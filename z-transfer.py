#!/usr/bin/python
########################################################
# ztransfer.py
# Adiel Ribeiro
# 07nov2022
# contato@nuvym.net
# v1
#######################################################
import os,sys
######################################################
sys.path.append('/offsec/desec/infra_gathering')
#################################################################
## var ## 
ALVO = input('Digite o dominio:\n')
print('')
FILTER = ('| cut -d " " -f4') 
TMP = ('> /tmp/ztransfer')
TMP2 = ('/tmp/ztransfer')
HOST = ('host -t ns')
HOST2 = (HOST + ' ' + ALVO + ' ' + FILTER + ' ' + TMP) 
HOST3 = ('host -l -a')
HOST4 = (HOST3 + ' ' + ALVO)
########################################################################
os.system(HOST2) 
###################################################################
f = open(TMP2, "r")
for zone in f: 
 os.system(HOST3 + ' ' + ALVO + ' ' + zone) 
f.close