#include <stdio.h>
#include <math.h>

double get(double x, double y){
    return sqrt(pow(x,2)+pow(y,2));
}
double calc(double r,double x, double y){
    double ret=0.0;
    for(int i=0; i<r;i++){
        printf("lap: %d\n", i);
        ret = pow(ret,2) + get(x,y);
    }
    return ret;
}

int main(void){
    double x,y,r;
    int count = 0;
    for (;;) {
        count ++;
        x=0.0;y=0.0;r=0.0;
        if(fscanf(stdin,"%lf %lf %lf",&x,&y,&r) >0){
            if(x>=-3 && x<=3 && y>=-3 && y<=3 && r>=0 && r<=10000){
                fprintf(stderr, "%lf\n", sqrt(r*(pow(x,2)+pow(y,2))));
                fprintf(stderr, "%lf\n", calc(r,x,y));
                if(sqrt(r*(pow(x,2)+pow(y,2))) <= 2){
                    printf("Case %d: IN \n", count);
                }else
                    printf("Case %d: OUT\n", count);
            }else
                return -1;
        } else
            return -1;
    }
    return 0;
}
