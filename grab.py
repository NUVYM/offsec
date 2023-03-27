#!/usr/bin/python
##########################################################
# grab.py
# Adiel Ribeiro
# 24nov2022
# contato@nuvym.net
# v1
#######################################################
import os,sys
from datetime import date
#############################################################################################################
## var ## 
DOMINIO = input('Digite o dominio a ser pesquisado: ' '')
PROJETO = input('Digite o nome do projeto: ' '')
NSLOOKUP = ('nslookup') 
NSLOOKUP2 = ('/nslookup-') 
NSLOOKUP3 = ('/nslookup-filtered-')
WHOIS = ('whois')
WHOIS2 = ('/whois-')
WHOIS3 = ('/whois-ip-')
OUT = ('> /offsec/si/')
PATH = ('/offsec/si/')
FILTER = ('| grep "Address" | awk "NR > 1" | cut -d ":" -f2') 
TRANSFORM = ('| sed -e "s/^[ \t]*//"')
TODAY = date.today()
######################################################################################################
HEAD = ('head -n1')
PATH2 = (PATH + '' + PROJETO + '' + NSLOOKUP2 + '' + str(TODAY))
NMAP = ('nmap --script whois-ip -iL')
##########################################################################################################################################
HARVESTER = ('theHarvester -l 20 -b bing -d')
HARVESTER2 = ('theHarvester -l 20 -b yahoo -d')
HARVESTER3 = ('theHarvester -l 100 -b urlscan -d')
OUT2 = ('>> /offsec/si/')
HARVESTER4 = ('/harvester-out-')
HARVESTER5 = ('theHarvester -l 100 -b hunter -d')
HARVESTER6 = ('theHarvester -l 100 -b censys -d')
HARVESTER7 = ('theHarvester -l 100 -b github-code -d')
HARVESTER8 = ('theHarvester -l 100 -b rapiddns -d')
HARVESTER9 = ('theHarvester -l 400 -b virustotal -d')
##########################################################################################################################
HOST = ('host')
HOST2 = ('/host-')
#######################################################################################################################
try: 
    os.mkdir(PATH + '' + PROJETO) 
except OSError as error: 
    pass 
##################################################################################################################################
os.system(NSLOOKUP + ' ' + DOMINIO + ' ' + FILTER + ' ' + TRANSFORM + ' ' + OUT + '' + PROJETO + '' + NSLOOKUP2 + '' + str(TODAY))
##############################################################################################################################
os.system(WHOIS + ' ' + DOMINIO + ' ' + OUT + '' + PROJETO + '' + WHOIS2 + '' + str(TODAY))
###################################################################################################################################
os.system(HEAD + ' ' + PATH2 + ' ' + OUT + '' + PROJETO + '' + NSLOOKUP3 + '' + str(TODAY))
#########################################################################################################################
f = open(PATH + '' + PROJETO + '' + NSLOOKUP2 + '' + str(TODAY), "r")
print('')
print('O IP p/ ser consultado no WHOIS e: ' '')
str(print(f.readline()))
f.close()
#############################################################################################################################################
os.system(NMAP + ' ' + PATH + '' + PROJETO + '' + NSLOOKUP3 + '' + str(TODAY) + ' ' + OUT + '' + PROJETO + '' + WHOIS3 + '' + str(TODAY))
##################################################################################################################################################
os.system(HARVESTER + ' ' + DOMINIO + ' ' + OUT2 + '' + PROJETO + '' + HARVESTER4 + '' + str(TODAY))
os.system(HARVESTER2 + ' ' + DOMINIO + ' ' + OUT2 + '' + PROJETO + '' + HARVESTER4 + '' + str(TODAY))
os.system(HARVESTER3 + ' ' + DOMINIO + ' ' + OUT2 + '' + PROJETO + '' + HARVESTER4 + '' + str(TODAY))
os.system(HARVESTER5 + ' ' + DOMINIO + ' ' + OUT2 + '' + PROJETO + '' + HARVESTER4 + '' + str(TODAY))
os.system(HARVESTER6 + ' ' + DOMINIO + ' ' + OUT2 + '' + PROJETO + '' + HARVESTER4 + '' + str(TODAY))
os.system(HARVESTER7 + ' ' + DOMINIO + ' ' + OUT2 + '' + PROJETO + '' + HARVESTER4 + '' + str(TODAY))
os.system(HARVESTER8 + ' ' + DOMINIO + ' ' + OUT2 + '' + PROJETO + '' + HARVESTER4 + '' + str(TODAY))
os.system(HARVESTER9 + ' ' + DOMINIO + ' ' + OUT2 + '' + PROJETO + '' + HARVESTER4 + '' + str(TODAY))
###############################################################################################################################
os.system(HOST + ' ' + DOMINIO + ' ' + OUT + '' + PROJETO + '' + HOST2 + '' + str(TODAY))
###########################################################################################################
