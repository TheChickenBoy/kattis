#include <stdio.h>

int main(void){
    int s=0,r1=0;
    if(fscanf(stdin,"%d %d", &r1,&s))
        printf("%d\n", (2*s)-r1);
    return 0;
}
