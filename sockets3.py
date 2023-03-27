#!/usr/bin/python
########################################################
# socket.py
# Adiel Ribeiro
# 06out2022
# contato@nuvym.net
# v1
#######################################################
import socket,sys  
###########################################################
## var ## 
IP = input('Digite o IP:' ' ')
PORTA = int(input('Digite a porta:' ' '))
MYSOCKET = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
ANSWER = MYSOCKET.connect_ex((IP,PORTA))
#########################################################

if (ANSWER == 0):
        print('Porta aberta')
else:
        print('Porta fechada')