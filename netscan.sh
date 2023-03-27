# Netscan
# Adiel Ribeiro
# 20set2022
# contato@nuvym.net
#################################################
#!/bin/bash
#################################################
if [ "$1" == "" ]
then
     echo "Modo de uso: $0 dominio"
else
wget $1 
fi 
if [ -f index.html ]
then
     grep "href" index.html | cut -d "/" -f 3 | grep "\." | cut -d '"' -f 1 | grep -v "<l" | cut -d ":" -f 1 > lista
     echo "Enderecos e IPs encontrados para $1"
     echo ""
     for url in $(cat lista);
do 
     host $url | grep -v "NXDOMAIN" | grep -v "alias"; 
     rm -f index.html
     rm -f lista 
done
else 
     rm -f index.html
     rm -f lista 
     exit 0
fi
     


