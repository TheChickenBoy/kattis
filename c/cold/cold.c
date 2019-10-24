#include <stdio.h>

int main(void){
    int n=0,nr=0,t=0;
    if(fscanf(stdin,"%d",&n))
        for(int i=0;i<n;i++)
            if(fscanf(stdin,"%d",&t))
                if(t<0)
                    nr++;

    printf("%d\n", nr);
    return 0;
}
