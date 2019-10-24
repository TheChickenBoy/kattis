#include <stdio.h>

int main(void){
    int l=0,r=0;
    if(fscanf(stdin,"%d %d",&l,&r)){
        if(l==r && l==0)
            printf("Not a moose\n");
        else if(l==r)
            printf("Even %d\n", l+r);
        else if(l>r)
            printf("Odd %d\n", l*2);
        else
            printf("Odd %d\n", r*2);
    }
    return 0;
}
