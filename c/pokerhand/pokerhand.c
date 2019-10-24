#include <stdio.h>

int main(void){
    char cards[1000]={0};
    unsigned char k1[3]={'\0'},k2[3]={'\0'},k3[3]={'\0'},k4[3]={'\0'},k5[3]={'\0'};
    if(fscanf(stdin,"%s %s %s %s %s",k1,k2,k3,k4,k5)){
        cards[k1[0]]++; cards[k2[0]]++; cards[k3[0]]++; cards[k4[0]]++; cards[k5[0]]++;
    }
    int v = cards[0];
    for(int i=1;i<1000;i++){
        if(v<cards[i])
            v = cards[i];
    }
    printf("%d\n", v);
    return 0;
}
