#include <stdio.h>

int main(void){
    int n=0,t=0;
    if(fscanf(stdin,"%d",&n))
        for(int i=0;i<n;i++)
            if(fscanf(stdin,"%d",&t)){
                if(t%2==0)
                    printf("%d is even\n", t);
                else
                    printf("%d is odd\n", t);
            }
}
