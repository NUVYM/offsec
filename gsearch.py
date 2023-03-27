#!/usr/bin/python
##########################################################
# gsearch.py
# Adiel Ribeiro
# 13nov2022
# contato@nuvym.net
# v1
#######################################################
import os
## var ## 
TERMO = input('Digite o termo a ser pesquisado: ' '')
GOOGLE = ('chromium https://google.com/search?q=')
##########################################################################
os.system(GOOGLE + '' + TERMO)