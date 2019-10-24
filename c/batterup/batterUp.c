#include <stdio.h>

int main(void){

    float n=0,temp=0.0,tot=0.0,min=0.0;
    if(fscanf(stdin,"%f",&n)>0){
        for(int i=0;i<n;i++)
            if(fscanf(stdin,"%f",&temp)>0){
                if(temp==-1)
                    min++;
                else
                    tot+=temp;

            }
        printf("%f\n", tot/(n-min));
    }
    return 0;
}
