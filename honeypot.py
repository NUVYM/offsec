#!/usr/bin/python
########################################################
# honeypot.py
# Adiel Ribeiro
# 26out2022
# contato@nuvym.net
# v1
#######################################################
import os,sys
###########################################################
## var ##
NC = ('nc -vnlp')
FTP = 21
SSH = 22
SMTP = 25
BG = ('&')
NETSTAT = ('netstat -nlpt')
SLEEP = ('sleep 2')
BANNER_FTP = ('< ftp.txt')
LOG_FTP = ('1>> ftp.log')
LOGERR_FTP = ('2>> ftp_err.log')
DATA = os.system('echo $(date) >> ftp.log')
LOGERR_SMTP = ('2>> smtp_err.log')
PS = os.system('for process in `ps aux | grep "nc -vnlp" | awk "{print $2}" | grep -v "grep"`; do `kill -9 $process 2> /dev/null`; done') 
################################################################################################################
#PS
###############################################################################################################
print('')
print('Abrindo portas:\n', FTP, SMTP)
print('')
#################################################################################################################
while True:
	os.system(NC + ' ' + str(FTP) + ' ' + BANNER_FTP  + ' ' + LOG_FTP + ' ' + LOGERR_FTP + ' ' + BG)
	DATA 
	os.system(SLEEP)
	#os.system(NC + ' ' + str(SSH) + ' ' + BG)
	os.system(NC + ' ' + str(SMTP) + ' ' + LOGERR_SMTP + ' ' + BG)
	os.system(SLEEP)
############################################################################################################
#print('')
#print('Portas abertas:\n')
#os.system(NETSTAT)