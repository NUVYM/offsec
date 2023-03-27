#!/usr/bin/python
########################################################
# hexconv.py
# Adiel Ribeiro
# 07nov2022
# contato@nuvym.net
# v1
#######################################################
import os 
###########################################################
## var ##
print('')
HEXA = input('Entre com o caminho do hexadecimal: ' '\n') 
print('')
CONV = ('xxd -r -p')
####################################################################
f = open(HEXA, "r")
print('')
os.system(CONV + ' ' + HEXA)
print('')