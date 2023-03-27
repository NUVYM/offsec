#!/usr/bin/python
########################################################
# web.py
# Adiel Ribeiro
# 06out2022
# contato@nuvym.net
# v1
#######################################################
import requests,urllib
######################################################
## var ## 
ENDERECO = input('Digite o endereco completo: ' '')
SITE = requests.get(ENDERECO)
STATUS = SITE.status_code
SERVICE = SITE.headers['Server']
WEB = urllib.request.urlopen(ENDERECO)
URL = WEB.geturl()
################################################################
if (STATUS == 200):
    print('Pagina', URL, 'existe\n')
else:
    print('Pagina nao existe\n')

print('O servidor e:', SERVICE) 

