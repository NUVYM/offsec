#!/usr/bin/python
##########################################################
# bsearch.py
# Adiel Ribeiro
# 13nov2022
# contato@nuvym.net
# v1
#######################################################
import os
## var ## 
TERMO = input('Digite o termo a ser pesquisado: ' '')
GOOGLE = ('chromium https://bing.com/search?q=')
##########################################################################
os.system(GOOGLE + '' + TERMO)