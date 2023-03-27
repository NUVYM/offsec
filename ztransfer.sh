#!/bin/bash
PATH=$PATH:/offsec/desec/infra_gathering
##########################################################
# ztransfer.sh
# Adiel Ribeiro
# 07dez2022
# contato@nuvym.net
# v1
###########################################################
for server in $(host -t ns $1 | cut -d " " -f4);
do
host -l -a $1 $server 
done
