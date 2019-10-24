#include <stdio.h>

int main(void){
    int l=0;
    double c=0,w=0,b=0,sum=0;

    if(fscanf(stdin,"%lf", &c))
        if(fscanf(stdin,"%d", &l))
            for(int i=0;i<l;i++)
                if(fscanf(stdin,"%lf %lf",&w,&b)){
                    sum = sum + (w*b*c);
            }

    printf("%.7lf\n", sum);
    return 0;
}
