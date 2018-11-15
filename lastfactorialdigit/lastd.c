#include <stdio.h>

int main(void){
    int n=0,t=0,sum=1;
    if(fscanf(stdin,"%d",&n))
        for(int i=0;i<n;i++)
            if(fscanf(stdin,"%d",&t)){
                for(int j=1;j<=t;j++)
                    sum = sum*j;
                printf("%d\n",sum%10);
                sum = 1;
            }
}
