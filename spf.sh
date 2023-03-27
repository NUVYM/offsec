#!/bin/bash
PATH=$PATH:/offsec/desec/infra_gathering/
##########################################################
# spf.sh
# Adiel Ribeiro
# 28dez2022
# contato@nuvym.net
# v1
###########################################################
echo "Entre com o dominio"
read dominio
###########################################################
rm -rf /tmp/spf-`date +%F`
#######################################################################################
host -t txt $dominio >> /tmp/spf-`date +%F`
echo ""
echo "Configuracao SPF"
echo ""
cat /tmp/spf-`date +%F` | grep "v=spf" 
echo ""