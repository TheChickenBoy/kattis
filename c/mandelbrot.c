#include <stdio.h>
#include <math.h>

int main(void){
    double x,y,r;
    int count = 0;
    for (;;) {
        count ++;
        x=0.0;y=0.0;r=0.0;
        if(fscanf(stdin,"%lf %lf %lf",&x,&y,&r) >0){
            if(x>=-3 && x<=3 && y>=-3 && y<=3 && r>=0 && r<=10000){
                if(sqrt(r*sqrt((pow(x,2)+pow(y,2)))) <= 2){
                    printf("Case %d: IN \n", count);
                }else
                    printf("Case %d: OUT\n", count);
            }else
                return 0;
        } else
            break;
    }
    return 0;
}
