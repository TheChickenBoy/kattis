#include <stdio.h>
#include <math.h>

int main(void){
    int h=0,v=0;
    double l=0;
    if(fscanf(stdin,"%d %d",&h,&v)){
        int x = 180-(v+90);
        l = h/cos(x*(M_PI/180));
        if(l>(int)l)
            l++;
        printf("%d\n", (int)l);
    }
}
