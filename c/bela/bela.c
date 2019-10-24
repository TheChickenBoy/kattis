#include <stdio.h>

int main(void){
    //char in[2] = {'\0'};
    int n=0;
    char suit = '\0';
    /*if(fscanf(stdin,"%d ",&n)>0){
        if(fscanf(stdin,"%s", &suit))
            printf("%d -%s-\n",n,&suit);
    }*/
    char in[3]={'\0'};
    if(fgets(in,3+1,stdin) != NULL){
        printf("%s %s\n", &in[0],&in[2]);
    }
    return 0;
}
