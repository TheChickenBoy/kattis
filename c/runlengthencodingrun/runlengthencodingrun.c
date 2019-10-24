#include <stdio.h>

int encode(int i, char str[]){
    char out[1000]={'\0'};
    int nr=0;
    char c,nc;
    char tmp='0';

    for(int j=0;i<1000;){
        c = str[i];
        if(c=='\0'||c=='\n')
            break;
        nr=1;
        do{
            nc=str[++i];
            if(nc==c)
                nr++;
        }while(c==nc);
        out[j++]=c;
        out[j++]=tmp+nr;
    }
    printf("%s\n",out);
    return 0;
}

int decode(int i, char str[]){
    char out[1000]={'\0'};
    int nr=0;
    char c,nc;

    for(int j=0;i<1000;){
        c = str[i++];
        nc = str[i++];
        if(c=='\0'||c=='\n')
            break;
        nr = nc-'0';
        for(int x=0;x<nr;x++)
            out[j++]=c;
    }

    printf("%s\n",out);

    return 0;
}
int main(void){
    char str[1000]={'\0'};

    if(fgets(str,1000,stdin) != NULL){
        int i=0;
        if(str[i]=='E'){
            i=2;
            encode(i,str);
        }else{
            i=2;
            decode(i,str);
        }
    }
    return 0;
}
