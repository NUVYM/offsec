#!/usr/bin/python
##########################################################
# lsearch.py
# Adiel Ribeiro
# 13nov2022
# contato@nuvym.net
# v1
#######################################################
import os
## var ## 
TERMO = input('Digite o dominio a ser pesquisado: ' '')
GOOGLE = ('lynx --dump https://google.com/search?q="site:')
EXT = ('ext:doc | ext:docx | ext:odt | ext:pdf | ext:csv | ext:xls | ext:xlsx | ext:ppt | ext:pptx | ext:txt | ext:ovpn | ext:conf | ext:cnf | ext:config | ext:pem | ext:crt | ext:key"')
FILTER = ('| cut -d "=" -f2 | egrep -v "site|google" | egrep "http|https" | sed "s/...$//"')
RESULT = ('> tmp/lsearch_result')
MKDIR = ('mkdir ./tmp 2> /dev/null')
RM = ('rm -rf ./tmp/*')
FILE = ('./tmp/lsearch_result')
WGET = ('wget --no-check-certificate -P ./tmp')
SCAN = ('exiftool')
DIR = ('./tmp/*')
RESULT2 = ('> tmp/exif_result')
SLEEP = ('sleep 3')
##########################################################################
print('')
os.system(MKDIR)
os.system(RM)
os.system(GOOGLE + '' + TERMO + ' ' + EXT + ' ' + FILTER + ' ' + RESULT)  
print('')
os.system(SLEEP)
########################################################################################################################
f = open(FILE, "r")
for file in f:
    os.system(WGET + ' ' + file)
f.close()
os.system(SLEEP)
#########################################################################################################################
os.system(SCAN + ' ' + DIR  + ' ' + RESULT2)