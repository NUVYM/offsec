#!/usr/bin/python
########################################################
# consulta.py
# Adiel Ribeiro
# 06out2022
# contato@nuvym.net
# v1
#######################################################
import socket,sys
######################################################
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("whois.iana.org",43))
s.send(bytes(sys.argv[1]+"\r\n", encoding='utf-8'))
resposta = s.recv(1024).split()
whois = (resposta[19])
print(whois.decode())
###########################################################
s1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s1.connect((whois,43))
s1.send(bytes(sys.argv[1]+"\r\n", encoding='utf-8'))
resp = s1.recv(1024)
print(resp.decode())