#!/bin/bash
PATH=$PATH:/offsec/desec/infra_gathering/
##########################################################
# revdns.sh
# Adiel Ribeiro
# 28dez2022
# contato@nuvym.net
# v1
###########################################################
echo "Entre com a rede"
read rede 
echo "Entre com o range de ips"
read ips 
###########################################################
rm -rf /tmp/revscan-`date +%F`
#######################################################################################
for scan in $(seq $ips);
do
host $rede.$scan >> /tmp/revscan-`date +%F`
done
echo ""
echo "Dominios encontrados"
echo ""
cat /tmp/revscan-`date +%F` | grep -v "$rede" | cut -d " " -f5
echo ""