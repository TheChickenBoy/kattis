#include <stdio.h>

int main(void){
    int h=0,m=0,um=0,uh=0;
    if(fscanf(stdin,"%d %d",&h,&m)){
        um=m-45;
        if(um<0){
            uh=h-1;
            um=60+um;
            if(uh<0)
                uh=23;

            printf("%d %d\n", uh,um);
            return 0;
        }else
            printf("%d %d\n", h,um);
    }
}
