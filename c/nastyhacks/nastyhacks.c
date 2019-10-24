#include <stdio.h>

int main(void){
    int n=0,r=0,e=0,c=0;
    if(fscanf(stdin,"%d", &n))
        for(int i=0;i<n;i++)
            if(fscanf(stdin,"%d %d %d", &r,&e,&c)){
                if(r<(e-c))
                    printf("advertise\n");
                else if(r==(e-c))
                    printf("does not matter\n");
                else
                    printf("do not advertise\n");
            }
    return 0;
}
