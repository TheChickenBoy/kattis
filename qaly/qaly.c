#include <stdio.h>

int main(void){
    int n = 0;
    double a=0.0,b=0.0,sum=0.0;

    if(fscanf(stdin,"%d",&n)){
        for(int i=0;i<n;i++){
            if(fscanf(stdin,"%lf %lf",&a,&b)){
                sum= sum + (a*b);
            }
        }
    }
    printf("%lf\n", sum);
    return 0;
}
