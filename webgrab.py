#!/usr/bin/python
########################################################
# webgrab.py
# Adiel Ribeiro
# 03nov2022
# contato@nuvym.net
# v1
#######################################################
import sys,os
###########################################################
## var ## 
NC = ('nc -i 1')
CALL = ('python /offsec/desec/lab/ctf1/webgrab.py')
NULL = ('2> /dev/null')
#########################################################
print("                                                                ")
print("                 ..:: NUVYM ::..                                ")
print("                                                                ")
print("  [0] Print Options                                             ")
print("  [1] SCAN                                                      ")
print("  [999] Exit                                                    ")
print("                                                                ")
################################################################################################
def menu():

    option = input('Please, select the option: ')

    match option:

        case "0":
            print("                                                                ")
            print("                 ..:: NUVYM ::..                                ")
            print("                                                                ")
            print("  [0] Print Options                                             ")
            print("  [1] SCAN                                                      ")
            print("  [999] Exit                                                    ")
            print("                                                                ")
            menu()

        case "1": 
            print('') 
            IP = input('Enter address:' ' ')
            PORT = int(input('Enter port:' ' '))           
            print('')
            os.system(NC + ' ' + IP + ' ' + str(PORT) + ' ' + NULL)
            print('')
            os.system(CALL)
            print('')
            menu()

        case "999":
            print('')
            print("GoodBye!")
            print('')
            sys.exit()

        case other:
            print('')
            print ('Invalid Option')
            print('')
            menu()

menu()


