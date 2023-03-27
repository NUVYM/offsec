#!/usr/bin/python
########################################################
# services.py
# Adiel Ribeiro
# 06out2022
# contato@nuvym.net
# v1
#######################################################
import socket
###########################################################
## var ##
IP = input('Digite o IP: ' '') 
PORTA = int(input('Digite a porta: ' ''))
MYSOCKET = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
ANSWER = MYSOCKET.connect((IP,PORTA))
BANNER = MYSOCKET.recv(1024)
##############################################################
print(BANNER)

print('Enviando usuario')
MYSOCKET.send(b'USER Ricado\r\n')
BANNER = MYSOCKET.recv(1024)
print(BANNER)

print('Enviando senha')
MYSOCKET.send(b'PASS 12345678\r\n')
BANNER = MYSOCKET.recv(1024)
print(BANNER)