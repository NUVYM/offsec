// portscan
// Adiel Ribeiro
// 29set2022
// contato@nuvym.net
///////////////////////////////////////////////////////////////////////////////////////////////
#include <stdio.h>
#include <sys/socket.h> 
#include <netdb.h>

int main(int argc, char *argv[]){

    int mysocket;
    int conexao;
    int porta;
    int inicio = 0;
    int fim = 80; 
    char *destino; 
    destino = argv[1];

    struct sockaddr_in alvo; 

    for(porta=inicio;porta<fim;porta++){

    mysocket = socket(AF_INET,SOCK_STREAM,0);
    alvo.sin_family = AF_INET;
    alvo.sin_port = htons(porta);
    alvo.sin_addr.s_addr = inet_addr(destino);

    conexao = connect(mysocket, (struct sockaddr *)&alvo, sizeof alvo);

    if(conexao == 0){
        printf("Porta %d [ABERTA] \n",porta);
        close(mysocket);
        close(conexao);
    } else {
                close(mysocket);
                close(conexao);
    }
    }
}

